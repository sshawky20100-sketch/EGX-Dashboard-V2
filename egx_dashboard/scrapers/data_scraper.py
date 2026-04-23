"""
EGX Stock Data Scraper  — Full Universe Edition
================================================
Sources (tried in order, first success wins):
  1. Yahoo Finance JSON API  — realtime quotes & history
  2. Mubasher.info HTML      — EGX-specific market watch
  3. Full offline demo data  — always works, seeded from real prices

Data is cached to disk (data/cache/) to avoid hammering sources on every page
refresh.  Cache TTL: 15 minutes for quotes, 24 hours for history.
"""

import os, sys, json, time, random, logging, hashlib
import requests, numpy as np, pandas as pd
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from typing import Optional, Dict, List

# ── project root on path ──────────────────────────────────────────────────
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from data.egx_universe import EGX_FULL_UNIVERSE, get_symbol_lookup

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

CACHE_DIR   = os.path.join(ROOT, "data", "cache")
os.makedirs(CACHE_DIR, exist_ok=True)

QUOTE_TTL   = 15 * 60        # 15 min in seconds
HISTORY_TTL = 24 * 60 * 60  # 24 h  in seconds

# ── HTTP helpers ─────────────────────────────────────────────────────────────
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0",
]

def _headers() -> Dict:
    return {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
        "DNT": "1",
    }

def _safe_get(url: str, timeout=14, retries=3, json_=False):
    for attempt in range(retries):
        try:
            time.sleep(random.uniform(0.4, 1.2))
            r = requests.get(url, headers=_headers(), timeout=timeout)
            r.raise_for_status()
            return r.json() if json_ else r
        except Exception as e:
            logger.debug(f"[{attempt+1}/{retries}] {url} -> {e}")
            if attempt < retries - 1:
                time.sleep(2 ** attempt)
    return None


# ══════════════════════════════════════════════════════════════════════════════
# DISK CACHE
# ══════════════════════════════════════════════════════════════════════════════
def _cache_path(key: str) -> str:
    h = hashlib.md5(key.encode()).hexdigest()[:12]
    return os.path.join(CACHE_DIR, f"{h}.json")

def _cache_read(key: str, ttl: int):
    p = _cache_path(key)
    if not os.path.exists(p):
        return None
    try:
        if time.time() - os.path.getmtime(p) > ttl:
            return None
        with open(p) as f:
            return json.load(f)
    except Exception:
        return None

def _cache_write(key: str, data):
    try:
        with open(_cache_path(key), "w") as f:
            json.dump(data, f)
    except Exception as e:
        logger.debug(f"Cache write error: {e}")


# ══════════════════════════════════════════════════════════════════════════════
# SCRAPER A — Yahoo Finance
# ══════════════════════════════════════════════════════════════════════════════
def _yahoo_quote(sym: str) -> Optional[Dict]:
    url  = (f"https://query1.finance.yahoo.com/v8/finance/chart/{sym}.CA"
            f"?interval=1d&range=1d&includePrePost=false")
    data = _safe_get(url, json_=True)
    if not data:
        return None
    try:
        meta = data["chart"]["result"][0]["meta"]
        prev = float(meta.get("chartPreviousClose") or meta.get("previousClose") or 1)
        cur  = float(meta.get("regularMarketPrice") or 0)
        if cur <= 0:
            return None
        return {
            "price":      round(cur, 2),
            "change":     round(cur - prev, 2),
            "change_pct": round((cur - prev) / prev * 100, 2),
            "volume":     int(meta.get("regularMarketVolume", 0)),
            "market_cap": int(meta.get("marketCap", 0)),
        }
    except Exception:
        return None


def _yahoo_history(symbol: str, days: int) -> pd.DataFrame:
    end   = int(datetime.now().timestamp())
    start = int((datetime.now() - timedelta(days=days + 30)).timestamp())
    url   = (f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}.CA"
             f"?interval=1d&period1={start}&period2={end}")
    data  = _safe_get(url, json_=True)
    if not data:
        return pd.DataFrame()
    try:
        res = data["chart"]["result"][0]
        ts  = res["timestamp"]
        q   = res["indicators"]["quote"][0]
        df  = pd.DataFrame({
            "date":   pd.to_datetime(ts, unit="s").date,
            "open":   q.get("open",  []),
            "high":   q.get("high",  []),
            "low":    q.get("low",   []),
            "close":  q.get("close", []),
            "volume": q.get("volume",[]),
        }).dropna()
        df = df[df["close"] > 0].tail(days).reset_index(drop=True)
        for c in ["open","high","low","close"]:
            df[c] = df[c].round(2)
        return df
    except Exception as e:
        logger.debug(f"Yahoo history parse error {symbol}: {e}")
        return pd.DataFrame()


# ══════════════════════════════════════════════════════════════════════════════
# SCRAPER B — Mubasher
# ══════════════════════════════════════════════════════════════════════════════
def _scrape_mubasher() -> Dict[str, Dict]:
    resp = _safe_get("https://www.mubasher.info/countries/eg/stocks/market-watch")
    if not resp:
        return {}
    soup    = BeautifulSoup(resp.text, "lxml")
    results = {}
    for tbl in soup.find_all("table"):
        for tr in tbl.find_all("tr")[1:]:
            tds = tr.find_all("td")
            if len(tds) < 5:
                continue
            try:
                sym = tds[0].get_text(strip=True).upper()
                px  = _pf(tds[2].get_text(strip=True))
                if px > 0 and sym:
                    results[sym] = {
                        "price":      px,
                        "change":     _pf(tds[3].get_text(strip=True)),
                        "change_pct": _pf(tds[4].get_text(strip=True).replace("%","")),
                        "volume":     _pv(tds[5].get_text(strip=True)) if len(tds) > 5 else 0,
                    }
            except Exception:
                continue
    return results


# ══════════════════════════════════════════════════════════════════════════════
# MASTER QUOTE FETCHER
# ══════════════════════════════════════════════════════════════════════════════
def fetch_all_stocks(force_refresh: bool = False) -> pd.DataFrame:
    """
    Fetches current quotes for the full EGX universe (195 stocks).
    Strategy:
      1. Disk cache (15 min TTL)
      2. Yahoo Finance per symbol
      3. Mubasher.info fallback
      4. Deterministic daily simulation for remaining gaps
    """
    if not force_refresh:
        cached = _cache_read("egx_all_stocks", QUOTE_TTL)
        if cached:
            logger.info("Returning cached market data")
            return pd.DataFrame(cached)

    lookup  = get_symbol_lookup()
    symbols = list(lookup.keys())
    logger.info(f"Fetching live quotes for {len(symbols)} EGX stocks...")

    # Step 1: Yahoo for first 80 symbols (rate limit aware)
    yahoo_hits: Dict[str, Dict] = {}
    for sym in symbols[:80]:
        q = _yahoo_quote(sym)
        if q:
            yahoo_hits[sym] = q
        time.sleep(0.5)
    logger.info(f"  Yahoo: {len(yahoo_hits)} live quotes")

    # Step 2: Mubasher for any remaining
    mubasher_hits = _scrape_mubasher()
    logger.info(f"  Mubasher: {len(mubasher_hits)} quotes")

    # Step 3: Build all rows
    today_seed = int(datetime.now().strftime("%Y%m%d"))
    rows = []
    for sym, meta in lookup.items():
        base = meta["base_price"]

        if sym in yahoo_hits:
            q      = yahoo_hits[sym]
            price  = q["price"]
            chg    = q["change"]
            pct    = q["change_pct"]
            vol    = q.get("volume", 0) or int(np.random.uniform(50_000, 3_000_000))
            mktcap = q.get("market_cap") or meta["market_cap"]
            src    = "live"
        elif sym in mubasher_hits:
            q      = mubasher_hits[sym]
            price  = q.get("price", base)
            chg    = q.get("change", 0)
            pct    = q.get("change_pct", 0)
            vol    = int(q.get("volume", 0)) or int(np.random.uniform(50_000, 3_000_000))
            mktcap = meta["market_cap"]
            src    = "mubasher"
        else:
            # Deterministic daily simulation (same values all day, realistic)
            rng    = np.random.default_rng((hash(sym) ^ today_seed) % 2**31)
            pct    = float(np.clip(rng.normal(0.1, 2.1), -9.5, 9.5))
            price  = round(base * (1 + pct / 100), 2)
            chg    = round(price - base, 2)
            vol    = int(rng.integers(20_000, 8_000_000))
            mktcap = meta["market_cap"]
            src    = "simulated"

        rows.append({
            "symbol":      sym,
            "name":        meta["name"],
            "sector":      meta["sector"],
            "subsector":   meta["subsector"],
            "price":       round(max(float(price), 0.01), 2),
            "change":      round(float(chg), 2),
            "change_pct":  round(float(pct), 2),
            "volume":      int(vol),
            "market_cap":  int(mktcap),
            "source":      src,
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M"),
        })

    df = pd.DataFrame(rows).drop_duplicates("symbol").reset_index(drop=True)
    _cache_write("egx_all_stocks", df.to_dict("records"))
    live = sum(1 for r in rows if r["source"] == "live")
    logger.info(f"Total: {len(df)} stocks  ({live} live, {len(df)-live} simulated)")
    return df


# ══════════════════════════════════════════════════════════════════════════════
# HISTORICAL PRICE DATA
# ══════════════════════════════════════════════════════════════════════════════
def fetch_stock_history(symbol: str, days: int = 180) -> pd.DataFrame:
    cache_key = f"hist_{symbol}_{days}"
    cached    = _cache_read(cache_key, HISTORY_TTL)
    if cached:
        return pd.DataFrame(cached)

    df = _yahoo_history(symbol, days)
    if df.empty:
        df = _gbm_history(symbol, days)

    if not df.empty:
        _cache_write(cache_key, df.to_dict("records"))
    return df


def _gbm_history(symbol: str, days: int) -> pd.DataFrame:
    """Geometric Brownian Motion synthetic history — always works."""
    lookup     = get_symbol_lookup()
    base_price = lookup.get(symbol, {}).get("base_price", 10.0)
    rng        = np.random.default_rng(hash(symbol) % 2**31)
    mu, sigma  = 0.0002, 0.018
    dates      = pd.bdate_range(end=datetime.now(), periods=days)
    shocks     = rng.normal(mu - 0.5 * sigma**2, sigma, days)
    prices     = base_price * np.exp(np.cumsum(shocks))
    return pd.DataFrame({
        "date":   dates.date,
        "open":   np.round(prices * (1 + rng.uniform(-0.005, 0.005, days)), 2),
        "high":   np.round(prices * (1 + np.abs(rng.normal(0, 0.012, days))), 2),
        "low":    np.round(prices * (1 - np.abs(rng.normal(0, 0.012, days))), 2),
        "close":  np.round(prices, 2),
        "volume": rng.integers(30_000, 6_000_000, days),
    })


# ══════════════════════════════════════════════════════════════════════════════
# NEWS SCRAPER
# ══════════════════════════════════════════════════════════════════════════════
def scrape_financial_news(max_articles: int = 40) -> List[Dict]:
    cached = _cache_read("egx_news", 30 * 60)
    if cached:
        return cached

    articles = []
    for fn in [_news_daily_news_egypt, _news_ahram, _news_enterprise,
               _news_investing_rss, _news_reuters_egypt]:
        try:
            articles.extend(fn())
        except Exception as e:
            logger.debug(f"{fn.__name__}: {e}")
        if len(articles) >= max_articles:
            break

    seen, unique = set(), []
    for a in articles:
        key = a.get("title","")[:60].lower().strip()
        if key and key not in seen:
            seen.add(key)
            unique.append(a)

    result = unique[:max_articles]
    if result:
        _cache_write("egx_news", result)
    return result


def _news_daily_news_egypt() -> List[Dict]:
    resp = _safe_get("https://dailynewsegypt.com/category/business/stock-exchange/")
    if not resp: return []
    soup = BeautifulSoup(resp.text, "lxml")
    arts = []
    for a in soup.select("h2 a, h3 a, .entry-title a")[:12]:
        title = a.get_text(strip=True)
        href  = a.get("href","")
        if title and len(title) > 20:
            arts.append({"title":title,"summary":"","url":href,
                         "published":datetime.now().strftime("%Y-%m-%d"),"source":"Daily News Egypt"})
    return arts

def _news_ahram() -> List[Dict]:
    resp = _safe_get("https://english.ahram.org.eg/News/Economy.aspx")
    if not resp: return []
    soup = BeautifulSoup(resp.text, "lxml")
    arts = []
    for a in soup.select(".news-title a, h3 a, .story-title a")[:12]:
        title = a.get_text(strip=True)
        href  = a.get("href","")
        if href and not href.startswith("http"):
            href = "https://english.ahram.org.eg" + href
        if title and len(title) > 20:
            arts.append({"title":title,"summary":"","url":href,
                         "published":datetime.now().strftime("%Y-%m-%d"),"source":"Al-Ahram Online"})
    return arts

def _news_enterprise() -> List[Dict]:
    resp = _safe_get("https://enterprise.press/category/business/")
    if not resp: return []
    soup = BeautifulSoup(resp.text, "lxml")
    arts = []
    for a in soup.select("article h2 a, article h3 a")[:12]:
        title = a.get_text(strip=True)
        href  = a.get("href","")
        if title and len(title) > 20:
            arts.append({"title":title,"summary":"","url":href,
                         "published":datetime.now().strftime("%Y-%m-%d"),"source":"Enterprise Press"})
    return arts

def _news_investing_rss() -> List[Dict]:
    resp = _safe_get("https://www.investing.com/rss/news_301.rss")
    if not resp: return []
    soup = BeautifulSoup(resp.text, "xml")
    arts = []
    for item in soup.find_all("item")[:12]:
        title   = item.find("title")
        desc    = item.find("description")
        link    = item.find("link")
        pubdate = item.find("pubDate")
        if title:
            arts.append({
                "title":     title.get_text(strip=True),
                "summary":   BeautifulSoup(desc.get_text(strip=True),"lxml").get_text()[:300] if desc else "",
                "url":       link.get_text(strip=True) if link else "",
                "published": pubdate.get_text(strip=True)[:30] if pubdate else "",
                "source":    "Investing.com",
            })
    return arts

def _news_reuters_egypt() -> List[Dict]:
    resp = _safe_get("https://www.reuters.com/world/middle-east/egypt/")
    if not resp: return []
    soup = BeautifulSoup(resp.text, "lxml")
    arts = []
    for a in soup.select("a[data-testid='Heading']")[:10]:
        title = a.get_text(strip=True)
        href  = a.get("href","")
        if href and not href.startswith("http"):
            href = "https://www.reuters.com" + href
        if title and len(title) > 20:
            arts.append({"title":title,"summary":"","url":href,
                         "published":datetime.now().strftime("%Y-%m-%d"),"source":"Reuters"})
    return arts


# ══════════════════════════════════════════════════════════════════════════════
# UTILITIES
# ══════════════════════════════════════════════════════════════════════════════
def _pf(text: str) -> float:
    try:
        return float(str(text).replace(",","").replace("+","").strip())
    except Exception:
        return 0.0

def _pv(text: str) -> float:
    t = str(text).replace(",","").strip().upper()
    for s, m in [("B",1e9),("M",1e6),("K",1e3)]:
        if t.endswith(s):
            try: return float(t[:-1]) * m
            except Exception: return 0.0
    try:    return float(t)
    except: return 0.0

def clear_cache():
    """Force-clear all cached files."""
    for f in os.listdir(CACHE_DIR):
        if f.endswith(".json"):
            os.remove(os.path.join(CACHE_DIR, f))
    logger.info("Cache cleared")
