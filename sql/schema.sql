CREATE TABLE games (
    game_id INTEGER PRIMARY KEY,
    season INTEGER NOT NULL,
    game_date TEXT NOT NULL,
    opponent TEXT NOT NULL,
    location TEXT NOT NULL,
    oregon_score INTEGER NOT NULL,
    opponent_score INTEGER NOT NULL,
    result TEXT NOT NULL,
    margin INTEGER NOT NULL
);