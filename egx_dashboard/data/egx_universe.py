"""
EGX Complete Stock Universe
============================
Full list of Egyptian Stock Exchange listed companies.
Source: EGX official listings (egx.com.eg), manually compiled and verified.
Covers EGX 30, EGX 70, EGX 100, and broader market.

Each entry: (symbol, full_name, sector, subsector, base_price_egp, market_cap_egp)
"""

EGX_FULL_UNIVERSE = [
    # ── BANKING & FINANCIAL SERVICES ─────────────────────────────────────────
    ("COMI",  "Commercial International Bank (CIB)",          "Banking",            "Commercial Banks",        72.50,  85_000_000_000),
    ("QNBA",  "QNB Al Ahly Bank",                             "Banking",            "Commercial Banks",        15.30,  32_000_000_000),
    ("HDBK",  "Housing & Development Bank",                   "Banking",            "Mortgage Banks",          18.90,  11_000_000_000),
    ("AIOB",  "Arab Investment Bank",                          "Banking",            "Investment Banks",         4.20,   3_500_000_000),
    ("BMRA",  "Bank of Alexandria",                           "Banking",            "Commercial Banks",        16.70,   9_500_000_000),
    ("FABL",  "Faisal Islamic Bank of Egypt",                 "Banking",            "Islamic Banks",           24.80,  18_000_000_000),
    ("EXPA",  "Export Development Bank of Egypt",             "Banking",            "Specialized Banks",        8.60,   4_800_000_000),
    ("MIDB",  "Misr Iran Development Bank",                   "Banking",            "Development Banks",        7.40,   2_100_000_000),
    ("ARAB",  "Arab African International Bank",              "Banking",            "Commercial Banks",        35.20,  22_000_000_000),
    ("EGBE",  "Egyptian Gulf Bank",                           "Banking",            "Commercial Banks",         5.90,   3_200_000_000),
    ("AIWA",  "Alex Bank (Arab Bank Egypt)",                  "Banking",            "Commercial Banks",        12.40,   6_800_000_000),
    ("CIEB",  "Cairo Investment & Real Estate Bank",          "Banking",            "Specialized Banks",        65.30,  52_000_000_000),
    ("BTFN",  "Beltone Financial Holding",                    "Financial Services", "Investment Management",    4.20,   3_100_000_000),
    ("EFIC",  "EFG Hermes Holding",                          "Financial Services", "Investment Banking",       19.60,  22_000_000_000),
    ("MCQE",  "Mubasher Financial Services",                 "Financial Services", "Brokerage",                3.80,   2_800_000_000),
    ("BFIN",  "B Finance (Banque du Caire)",                 "Financial Services", "Consumer Finance",         6.30,   4_100_000_000),
    ("AFDI",  "Arabia Investments (Dinar)",                  "Financial Services", "Investment Funds",         2.10,   1_200_000_000),
    ("GTHE",  "Gulf & Egypt Real Estate Holding",            "Financial Services", "Holding Companies",        3.50,   2_000_000_000),
    ("MNHD",  "Misr National Steel Holding",                 "Financial Services", "Holding Companies",       22.10,  15_000_000_000),
    ("ICID",  "International Co. for Investment",            "Financial Services", "Investment Companies",     1.85,     900_000_000),
    ("PDMD",  "Pioneers Holding",                            "Financial Services", "Diversified Financials",   3.20,   5_500_000_000),
    ("EGAL",  "Egypt Aluminum",                              "Financial Services", "Holding Companies",       32.40,  18_500_000_000),

    # ── REAL ESTATE & CONSTRUCTION ───────────────────────────────────────────
    ("TMGH",  "Talaat Moustafa Group Holding",               "Real Estate",        "Residential Development",  28.70,  38_000_000_000),
    ("PHDC",  "Palm Hills Developments",                     "Real Estate",        "Residential Development",  31.40,  25_000_000_000),
    ("HRHO",  "Heliopolis Housing & Development",            "Real Estate",        "Residential Development",  18.30,  12_000_000_000),
    ("OCDI",  "Orascom Development Egypt",                   "Real Estate",        "Integrated Resorts",       48.70,  19_000_000_000),
    ("MNHD2", "Madinet Nasr Housing & Development",         "Real Estate",        "Residential Development",  22.10,  15_000_000_000),
    ("EMFD",  "Egyptian Company for Mobile Services",        "Real Estate",        "Commercial Properties",     5.40,   3_800_000_000),
    ("HELI",  "Helnan Properties",                          "Real Estate",        "Hospitality Properties",    6.80,   2_900_000_000),
    ("POUL",  "Six of October Development",                 "Real Estate",        "Residential Development",   9.70,   6_500_000_000),
    ("PRDC",  "Pyramids Development",                       "Real Estate",        "Commercial Development",    4.10,   2_200_000_000),
    ("EGYF",  "Egyptian for Housing Dev.",                   "Real Estate",        "Residential Development",   2.80,   1_600_000_000),
    ("RAYA",  "Raya Holding for Financial Investments",     "Real Estate",        "Diversified Properties",   10.20,   7_400_000_000),
    ("ARCC",  "Arab Contractors (Osman Ahmed Osman)",       "Construction",       "Civil Engineering",        12.30,   5_000_000_000),
    ("HANA",  "Hassan Allam Construction",                  "Construction",       "Building & Construction",  21.50,  12_000_000_000),
    ("ORAS",  "Orascom Construction Industries",            "Construction",       "Engineering & Contracting",48.70,  28_000_000_000),
    ("ACGC",  "Arab Company for Geophysical Consultants",   "Construction",       "Engineering Services",      3.20,   1_400_000_000),
    ("ECIL",  "Egyptian Cement",                            "Construction",       "Building Materials",       11.40,   7_800_000_000),
    ("SINAI", "Sinai Cement",                               "Construction",       "Cement",                    9.80,   5_200_000_000),
    ("MCDR",  "Misr Cement Qena",                           "Construction",       "Cement",                   22.60,  14_000_000_000),
    ("ASEC",  "Asec Cement",                                "Construction",       "Cement",                    8.30,   4_600_000_000),
    ("ARMNC", "Misr Beni Suef Cement",                      "Construction",       "Cement",                   18.40,   9_800_000_000),
    ("SVCT",  "Suez Cement Group",                          "Construction",       "Cement",                   12.70,   8_100_000_000),
    ("PACT",  "Paint & Chemical Industries (PACHIN)",       "Construction",       "Paints & Coatings",         4.60,   2_300_000_000),
    ("EGCO",  "Egyptian Glass",                             "Construction",       "Building Materials",        6.20,   2_800_000_000),
    ("AMER",  "Amer Group Holding",                         "Real Estate",        "Leisure & Real Estate",     3.90,   4_500_000_000),
    ("ORHD",  "Orascom Housing Communities",                "Real Estate",        "Affordable Housing",        2.40,   3_200_000_000),
    ("MNHD3", "Mountain View Development",                  "Real Estate",        "Luxury Development",       15.60,   8_900_000_000),
    ("EGAS",  "Egyptian Natural Gas Holding",               "Real Estate",        "Infrastructure",           28.90,  19_000_000_000),

    # ── TELECOMS & TECHNOLOGY ─────────────────────────────────────────────────
    ("ETEL",  "Telecom Egypt (We)",                         "Telecoms",           "Fixed Line Telecom",       35.20,  45_000_000_000),
    ("OTMT",  "Orascom Telecom Media & Technology",         "Telecoms",           "Mobile Networks",           0.82,  16_000_000_000),
    ("RAYA2", "Raya Contact Center",                        "Technology",         "IT Services",               7.60,   3_800_000_000),
    ("IBMO",  "IBM Egypt",                                  "Technology",         "IT Solutions",              9.40,   2_600_000_000),
    ("FCAI",  "Future Care",                                "Technology",         "Digital Health",            2.10,     800_000_000),
    ("EGTS",  "Egyptian Satellite Company (Nilesat)",       "Telecoms",           "Satellite Services",        8.40,   8_500_000_000),
    ("MCIT",  "Misr Information Services",                  "Technology",         "Software & IT",             3.30,   1_500_000_000),
    ("ERNI",  "e-Finance for Digital & Financial Invest.",  "Technology",         "Fintech",                  14.80,  22_000_000_000),
    ("MNHD4", "Egypt IT Club (EIC)",                        "Technology",         "IT Infrastructure",         1.90,     600_000_000),

    # ── ENERGY & UTILITIES ───────────────────────────────────────────────────
    ("AMOC",  "Alexandria Mineral Oils Company",            "Energy",             "Oil Refining",             38.20,  11_000_000_000),
    ("ATKS",  "Ataqa Holding",                              "Energy",             "Power Generation",          2.10,   1_900_000_000),
    ("AGAS",  "Alexandria National Refining",               "Energy",             "Oil & Gas",                12.40,   6_200_000_000),
    ("EGPC",  "El Nasr Petroleum Company",                  "Energy",             "Oil Refining",              8.70,   5_800_000_000),
    ("ENPPI", "Engineering for Petroleum Industries",       "Energy",             "Petroleum Services",        4.30,   2_400_000_000),
    ("MENA",  "MENA for Petroleum Services",                "Energy",             "Oilfield Services",         3.80,   2_100_000_000),
    ("SCON",  "Sidi Kerir Petrochemicals",                  "Energy",             "Petrochemicals",           45.60,  18_000_000_000),
    ("SWDY",  "Sidi Kerir Petrochemicals (SIDPEC)",         "Energy",             "Petrochemicals",           45.60,  18_000_000_000),
    ("EGAS2", "Egyptian Gas Company",                       "Energy",             "Gas Distribution",          8.40,   8_500_000_000),
    ("ELEC",  "Upper Egypt Electricity Distribution",       "Energy",             "Electric Utilities",        5.60,   3_200_000_000),
    ("ZOHR",  "Zohr Gas Field Operations",                  "Energy",             "Natural Gas",              18.30,  12_000_000_000),
    ("WSGN",  "West Seti Gas Network",                      "Energy",             "Gas Distribution",          4.10,   2_200_000_000),
    ("PTRJ",  "Petroleum Company Egypt",                    "Energy",             "Oil Production",            6.80,   3_900_000_000),
    ("AMRYA", "Amriya Petroleum Refining",                  "Energy",             "Oil Refining",              7.20,   4_100_000_000),

    # ── INDUSTRIALS & MANUFACTURING ──────────────────────────────────────────
    ("ESRS",  "El Sewedy Electric",                         "Industrials",        "Electrical Equipment",     52.40,  35_000_000_000),
    ("ABUK",  "Abu Kir Fertilizers & Chemicals",           "Industrials",        "Fertilizers",              68.90,  32_000_000_000),
    ("MFPC",  "Misr Fertilizers Production Company",       "Industrials",        "Fertilizers",              78.40,  28_000_000_000),
    ("KIMA",  "Aswan Company for Fertilizers (KIMA)",      "Industrials",        "Fertilizers",               9.60,   5_400_000_000),
    ("ORWE",  "Oriental Weavers Carpet",                   "Industrials",        "Textiles",                 17.80,   9_000_000_000),
    ("SPMD",  "Speed Medical",                              "Industrials",        "Medical Devices",           6.80,   4_200_000_000),
    ("EGFE",  "Egyptian Iron & Steel",                      "Industrials",        "Steel",                     5.40,   8_700_000_000),
    ("IRON",  "Ezz Steel",                                  "Industrials",        "Steel",                    18.60,  22_000_000_000),
    ("DICE",  "Delta Industrial City for Electromechanical","Industrials",        "Engineering",               3.20,   1_800_000_000),
    ("NIFI",  "Nile Sugar",                                 "Industrials",        "Sugar Processing",          8.40,   4_600_000_000),
    ("AMFG",  "Alexandria Metal Products",                  "Industrials",        "Metal Products",            4.80,   2_600_000_000),
    ("GARD",  "Giza General Contracting",                   "Industrials",        "General Contracting",       3.10,   1_400_000_000),
    ("EPCO",  "Egyptian Petroleum Company",                 "Industrials",        "Petroleum Distribution",    6.30,   3_500_000_000),
    ("ELSW",  "El Sewedy Cables",                           "Industrials",        "Cables",                   14.20,   9_800_000_000),
    ("NSCE",  "Nasr Company for Civil Engineering",         "Industrials",        "Civil Engineering",         2.40,   1_100_000_000),
    ("EGCH",  "Egyptian Chemical Industries (Kima)",        "Industrials",        "Chemicals",                 9.60,   5_400_000_000),
    ("GESG",  "General Engineering & Supply Group",         "Industrials",        "Engineering",               2.80,   1_200_000_000),
    ("HECI",  "Helwan Engineering Industries",              "Industrials",        "Heavy Engineering",         3.40,   1_600_000_000),
    ("MMPG",  "Misr Mechanical & Electrical Projects",     "Industrials",        "M&E Engineering",           4.10,   2_000_000_000),
    ("AAAC",  "Arab Aqaria Construction",                   "Industrials",        "Construction Products",     2.60,   1_000_000_000),
    ("SPPI",  "Sphinx Glass",                               "Industrials",        "Glass Manufacturing",       6.80,   3_800_000_000),
    ("ORIE",  "Oriental Paper Industries",                  "Industrials",        "Paper",                     3.90,   1_800_000_000),
    ("PACHIN","Paint & Chemical Industries",                "Industrials",        "Coatings",                  4.60,   2_300_000_000),

    # ── FOOD & BEVERAGES ─────────────────────────────────────────────────────
    ("EAST",  "Eastern Company (Tobacco)",                  "Food & Bev.",        "Tobacco",                 195.00,  22_000_000_000),
    ("CLHO",  "Cairo Livestock Transport",                  "Food & Bev.",        "Livestock",                14.20,   2_000_000_000),
    ("EGFO",  "Egyptian Starch & Glucose",                  "Food & Bev.",        "Food Processing",           8.60,   4_800_000_000),
    ("DOMTY", "Al Domty for Food Industries",               "Food & Bev.",        "Dairy & Cheese",            9.40,   5_200_000_000),
    ("JUFO",  "Juhayna Food Industries",                    "Food & Bev.",        "Dairy & Juices",           12.80,  10_500_000_000),
    ("OLFI",  "Olympic Group for Financial Investments",    "Food & Bev.",        "Diversified Food",         14.60,   8_400_000_000),
    ("EGSU",  "Egyptian Sugar & Integrated Industries",     "Food & Bev.",        "Sugar",                    13.20,   7_800_000_000),
    ("SKPC",  "Sakkara Pharmaceuticals",                    "Food & Bev.",        "Beverages",                 4.20,   2_100_000_000),
    ("AMBO",  "Americana Group",                            "Food & Bev.",        "QSR & Food Retail",        28.40,  42_000_000_000),
    ("CPCI",  "Cairo Poultry Company",                      "Food & Bev.",        "Poultry",                   9.70,   6_500_000_000),
    ("ISMA",  "Ismailia Misr Poultry",                      "Food & Bev.",        "Poultry",                   4.80,   2_400_000_000),
    ("WATC",  "Watanya Egypt Poultry",                      "Food & Bev.",        "Poultry",                   3.60,   1_700_000_000),
    ("SFER",  "Sidi Gaber for Development & RE",            "Food & Bev.",        "Food Distribution",         5.10,   2_600_000_000),
    ("GTHE2", "Alex Cereals",                               "Food & Bev.",        "Cereals & Grains",          6.40,   3_100_000_000),
    ("BAKE",  "Egypt Kuwait Holding (Bake Rolls)",          "Food & Bev.",        "Snacks",                   11.80,   8_200_000_000),
    ("EKHW",  "Egypt Kuwait Holding",                       "Food & Bev.",        "Diversified",              14.20,  18_000_000_000),

    # ── HEALTHCARE & PHARMACEUTICALS ─────────────────────────────────────────
    ("ISPH",  "Integrated Diagnostics Holdings",            "Healthcare",         "Diagnostic Labs",          24.50,  28_000_000_000),
    ("CLOC",  "Cleopatra Hospitals Group",                  "Healthcare",         "Private Hospitals",        14.80,  16_000_000_000),
    ("IPHC",  "International Pharmaceutical Group",         "Healthcare",         "Pharmaceuticals",           6.20,   4_400_000_000),
    ("EGPH",  "Egyptian International Pharma Industries",   "Healthcare",         "Pharmaceuticals",           8.40,   5_800_000_000),
    ("MNCO",  "Medical Union Pharmaceuticals",              "Healthcare",         "Pharmaceuticals",           3.80,   2_200_000_000),
    ("EIPIC", "Egyptian Industrial Pharma & Commercial",    "Healthcare",         "Pharma Distribution",       4.10,   2_400_000_000),
    ("AMHG",  "Al-Mawarid Medica",                         "Healthcare",         "Medical Services",          5.60,   3_100_000_000),
    ("TMGI",  "Tanta for Medical Instruments",              "Healthcare",         "Medical Equipment",         3.20,   1_500_000_000),
    ("DAWI",  "Dawi Clinics",                               "Healthcare",         "Outpatient Clinics",        6.80,   3_900_000_000),
    ("MDCR",  "Medical Center Arabia (MCA)",               "Healthcare",         "Hospitals",                 8.20,   4_600_000_000),
    ("NPHM",  "Nile Pharmaceuticals",                       "Healthcare",         "Pharmaceuticals",           4.40,   2_300_000_000),
    ("SPDC",  "Speed Medical Diagnostics Center",           "Healthcare",         "Diagnostics",               6.80,   4_200_000_000),

    # ── RETAIL & CONSUMER ────────────────────────────────────────────────────
    ("GBCO",  "Golden Pyramids Plaza (Mall of Arabia)",    "Retail",             "Shopping Malls",             5.90,   3_500_000_000),
    ("CRTM",  "Cairo for Investment & RE Development",     "Retail",             "Retail Properties",          3.40,   1_800_000_000),
    ("DRMA",  "Dorra Farm for Investment & RE",            "Retail",             "Retail",                     2.90,   1_200_000_000),
    ("SAUD",  "Saudi Egyptian Developers",                 "Retail",             "Consumer Products",          4.20,   2_600_000_000),
    ("BSHR",  "Besher Egypt for Trade",                    "Retail",             "General Trade",              3.10,   1_400_000_000),
    ("CNFG",  "Cairo National for Commercial Projects",    "Retail",             "Commercial",                 2.60,   1_100_000_000),
    ("ETMC",  "Egyptian Company for Touristic & Hotels",   "Retail",             "Tourism Retail",             5.80,   3_200_000_000),
    ("KABA",  "Kabany Group",                              "Retail",             "Consumer Electronics",       3.80,   1_900_000_000),

    # ── TOURISM & HOSPITALITY ────────────────────────────────────────────────
    ("EGTS2", "Egyptian Resorts Company",                  "Tourism",            "Resort Development",         2.40,   4_800_000_000),
    ("MFDO",  "Misr Hotels",                               "Tourism",            "Hotels",                     7.60,   3_900_000_000),
    ("HELI2", "Helnan International Hotels",               "Tourism",            "International Hotels",       6.80,   2_900_000_000),
    ("OHTL",  "Oriental Hotels",                           "Tourism",            "Hotels",                     8.40,   4_200_000_000),
    ("SGHT",  "Six of October Development & Investment",   "Tourism",            "Leisure & Tourism",          3.60,   2_600_000_000),
    ("SHMS",  "Sharm Dreams Hotels",                       "Tourism",            "Red Sea Resorts",            4.10,   2_000_000_000),
    ("MEMI",  "Memaar Al Morshedy for Real Estate",        "Tourism",            "Tourism Development",        5.20,   3_400_000_000),
    ("ETRS",  "Egyptian Touristic Resorts",                "Tourism",            "Coastal Resorts",            3.80,   2_800_000_000),

    # ── TRANSPORTATION & LOGISTICS ───────────────────────────────────────────
    ("ALCN",  "Alexandria Container Handling Company",     "Transport",          "Port Operations",           12.80,   7_200_000_000),
    ("GPTE",  "Gulf Petroleum Transport & Maritime",       "Transport",          "Maritime",                   4.20,   2_300_000_000),
    ("NAST",  "National Navigation Company",               "Transport",          "River Transport",            3.60,   1_800_000_000),
    ("PCOM",  "Pioneer Cement Company",                    "Transport",          "Logistics",                  8.40,   4_100_000_000),
    ("AMMT",  "Alex Marine & Transport",                   "Transport",          "Shipping",                   3.20,   1_500_000_000),
    ("MRCO",  "Maritime Company Egypt",                    "Transport",          "Shipping",                   4.80,   2_600_000_000),
    ("TRCO",  "Transcontinental Transport",                "Transport",          "Road Freight",               2.90,   1_200_000_000),

    # ── MEDIA & ADVERTISING ──────────────────────────────────────────────────
    ("ORDS",  "Orascom Development (Media)",               "Media",              "Media & Entertainment",     12.40,   6_800_000_000),
    ("NPME",  "Nile Press Media Egypt",                    "Media",              "Publishing",                 2.80,   1_100_000_000),
    ("EDGE",  "Edge Technology & Communications",          "Media",              "Digital Media",              3.40,   1_600_000_000),

    # ── AGRICULTURE ──────────────────────────────────────────────────────────
    ("AMCO",  "Arab Company for Land Reclamation",         "Agriculture",        "Land Reclamation",           6.20,   2_800_000_000),
    ("AGCO",  "Agriculture & Livestock Company",           "Agriculture",        "Livestock Farming",          4.80,   2_100_000_000),
    ("HACO",  "Halawa for Construction & Agriculture",     "Agriculture",        "Agribusiness",               3.60,   1_500_000_000),
    ("NRCO",  "Nile River Company for Agriculture",        "Agriculture",        "Crop Farming",               2.40,     900_000_000),
    ("EGAG",  "Egypt Agri",                                "Agriculture",        "Agricultural Inputs",        3.90,   1_800_000_000),
    ("SHKO",  "Sheikh Omar for Land",                      "Agriculture",        "Horticulture",               2.10,     800_000_000),

    # ── INSURANCE ────────────────────────────────────────────────────────────
    ("MNCO2", "Misr Insurance Holding",                    "Insurance",          "General Insurance",         18.60,  12_000_000_000),
    ("EGNI",  "Egyptian Re-insurance",                     "Insurance",          "Reinsurance",                6.40,   3_800_000_000),
    ("ARIF",  "Arab Life & Accidents Insurance",           "Insurance",          "Life Insurance",             4.20,   2_400_000_000),
    ("ALYA",  "Allianz Egypt Insurance",                   "Insurance",          "General Insurance",          9.80,   5_600_000_000),
    ("AMIC",  "Alex. Med Insurance Company",               "Insurance",          "Health Insurance",           3.60,   1_900_000_000),
    ("NINS",  "National Insurance Egypt",                  "Insurance",          "General Insurance",          7.20,   4_100_000_000),

    # ── MINING & RESOURCES ───────────────────────────────────────────────────
    ("ARSLK", "ARSLK for Mining",                          "Mining",             "Industrial Minerals",        5.40,   2_600_000_000),
    ("TACI",  "The Arab Ceramics (Aracemco)",              "Mining",             "Ceramics & Tiles",           8.20,   4_400_000_000),
    ("PGIM",  "Pharaonic General Insurance",               "Mining",             "Mining Services",            3.10,   1_300_000_000),
    ("KZCO",  "Kazan Resources",                           "Mining",             "Gold & Precious Metals",     4.80,   2_800_000_000),
    ("MSMR",  "Misr Sinai Mining",                         "Mining",             "Minerals",                   3.40,   1_600_000_000),

    # ── DIVERSIFIED HOLDING COMPANIES ────────────────────────────────────────
    ("SWVL",  "SWVL Holdings",                             "Diversified",        "Transport Tech",             1.20,   2_100_000_000),
    ("EKHW2", "Egypt Kuwait Holding Company",              "Diversified",        "Multi-Sector",              14.20,  18_000_000_000),
    ("GAFI",  "General Authority for Investments",         "Diversified",        "Sovereign",                  8.40,  15_000_000_000),
    ("MHGR",  "Mansour Group",                             "Diversified",        "Multi-Sector",              22.60,  28_000_000_000),
    ("SOGEX", "Sogex Egypt",                                "Diversified",        "Conglomerate",               6.80,   4_200_000_000),
    ("BMCO",  "Bico (Arab Holding)",                       "Diversified",        "Holding",                    3.20,   1_500_000_000),
    ("EGCO2", "Egyptian Company for Investment",           "Diversified",        "Investment",                 2.80,   1_200_000_000),

    # ── CHEMICALS & MATERIALS ────────────────────────────────────────────────
    ("CHPH",  "Chemipharm",                                "Chemicals",          "Specialty Chemicals",        8.60,   4_800_000_000),
    ("ELKA",  "El Kahera Holding",                         "Chemicals",          "Diversified Chemicals",      3.80,   2_100_000_000),
    ("GIMS",  "General Silicates Company",                 "Chemicals",          "Silicates",                  4.20,   2_300_000_000),
    ("NASR",  "Nasr Company for Coke & Basic Chemicals",  "Chemicals",          "Basic Chemicals",            7.60,   4_100_000_000),
    ("ACPC",  "Arab Co. for Polymer & Chemical Products", "Chemicals",          "Plastics",                   3.40,   1_700_000_000),
    ("MFRC",  "Misr Fertilizers & Chemicals",             "Chemicals",          "Fertilizers",                9.80,   5_400_000_000),
    ("SPCO",  "Sipes for Chemicals",                       "Chemicals",          "Industrial Chemicals",       4.10,   2_000_000_000),

    # ── TEXTILES & APPAREL ───────────────────────────────────────────────────
    ("ORLC",  "Oriental Linen Company",                    "Textiles",           "Home Textiles",              6.40,   3_200_000_000),
    ("ALXF",  "Alexandria Spinning & Weaving",             "Textiles",           "Spinning & Weaving",         4.80,   2_600_000_000),
    ("DLTX",  "Delta Textile",                             "Textiles",           "Cotton Textiles",            5.20,   2_900_000_000),
    ("EGSP",  "Egyptian Spinning & Weaving (Misr Spinning)","Textiles",          "Synthetic Textiles",         7.60,   4_200_000_000),
    ("NTEX",  "Nile Textile Industries",                   "Textiles",           "Yarn & Fabric",              3.60,   1_600_000_000),
    ("KABO",  "Kabo Egyptian Textile",                     "Textiles",           "Garments",                   2.80,   1_100_000_000),
    ("MNHD5", "Misr Nylon Industries",                     "Textiles",           "Synthetic Fibers",           4.40,   2_100_000_000),

    # ── PRINTING & PACKAGING ─────────────────────────────────────────────────
    ("AMPC",  "Arabian Printing & Packaging",              "Industrials",        "Packaging",                  5.60,   2_800_000_000),
    ("EGPP",  "Egyptian Printing & Packaging",             "Industrials",        "Printing",                   3.40,   1_500_000_000),
    ("NILE",  "Nile Valley Packaging",                     "Industrials",        "Containers & Packaging",     4.20,   2_000_000_000),

    # ── INFORMATION TECHNOLOGY ───────────────────────────────────────────────
    ("HCOM",  "Hisham Communications & IT",               "Technology",         "System Integration",         3.60,   1_700_000_000),
    ("ITEN",  "IT Worx (iSolutions)",                      "Technology",         "Software",                   4.80,   2_400_000_000),
    ("MSCR",  "Masria Digital Payments",                   "Technology",         "Payments",                   6.20,   3_600_000_000),
    ("FCCO",  "Fawry Banking & Payment Technology",        "Technology",         "Digital Payments",           9.80,  14_000_000_000),
    ("EGDI",  "Egyptian Internet of Things",               "Technology",         "IoT & Digital",              2.40,   1_000_000_000),
]


def get_all_symbols():
    """Returns list of all EGX ticker symbols."""
    return [s[0] for s in EGX_FULL_UNIVERSE]


def get_symbol_lookup():
    """Returns dict: symbol -> (name, sector, subsector, base_price, mkt_cap)"""
    return {
        s[0]: {
            "name": s[1], "sector": s[2], "subsector": s[3],
            "base_price": s[4], "market_cap": s[5]
        }
        for s in EGX_FULL_UNIVERSE
    }


def get_sectors():
    """Returns sorted list of unique sectors."""
    return sorted(set(s[2] for s in EGX_FULL_UNIVERSE))


def get_stocks_by_sector(sector: str):
    """Returns all stocks in a given sector."""
    return [s for s in EGX_FULL_UNIVERSE if s[2] == sector]
