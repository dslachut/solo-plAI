CREATE TABLE IF NOT EXISTS space77_starport_classes (
    class TEXT PRIMARY KEY,
    note TEXT NOT NULL
);

INSERT OR IGNORE INTO space77_starport_classes (class, note)
VALUES 
    ("A", "Best quality starport. Refined fuel, annual maintenance overhauls, and starship construction are available here."),
    ("B", "Good quality starport. Refined fuel, annual maintenance overhauls, and non-FTL spaceship construction are available here."),
    ("C", "Medium quality starport. Only unrefined fuel and basic repair facilities are available."),
    ("D", "Poor quality starport. Only unrefined fuel is available. No maintenance or special repair facilities are available."),
    ("E", "Open bedrock or concrete landing pad. No fuel or other starship support available."),
    ("X", "No support for starship landings.")
;
