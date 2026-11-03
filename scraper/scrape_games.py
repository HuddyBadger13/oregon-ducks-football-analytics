import re
from pathlib import Path

import pandas as pd


SEASONS = [2024, 2025]
OUTPUT_FILE = Path("data/games.csv")


def scrape_season(season):
    url = f"https://goducks.com/sports/football/schedule/text/{season}"

    print(f"Downloading {season} season...")
    tables = pd.read_html(url)

    schedule = None

    for table in tables:
        if "Opponent" in table.columns and "Result" in table.columns:
            schedule = table
            break

    if schedule is None:
        raise RuntimeError(f"Could not find the schedule table for {season}")

    games = []

    for _, row in schedule.iterrows():
        result_text = str(row["Result"]).strip()

        score_match = re.search(
            r"([WL])\s*(\d+)-(\d+)",
            result_text
        )

        if score_match is None:
            continue

        result = score_match.group(1)
        oregon_score = int(score_match.group(2))
        opponent_score = int(score_match.group(3))
        margin = oregon_score - opponent_score

        location_text = str(row.get("At", "")).lower()

        if "away" in location_text or "at" in location_text:
            location = "Away"
        elif "neutral" in location_text or "vs" in location_text:
            location = "Neutral"
        else:
            location = "Home"

        games.append({
            "season": season,
            "game_date": str(row["Date"]),
            "opponent": str(row["Opponent"]).strip(),
            "location": location,
            "oregon_score": oregon_score,
            "opponent_score": opponent_score,
            "result": result,
            "margin": margin
        })

    return games


all_games = []

for season in SEASONS:
    all_games.extend(scrape_season(season))

OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

games_dataframe = pd.DataFrame(all_games)
games_dataframe.insert(
    0,
    "game_id",
    range(1, len(games_dataframe) + 1)
)

games_dataframe.to_csv(OUTPUT_FILE, index=False)

print()
print(f"Saved {len(games_dataframe)} games to {OUTPUT_FILE}")
print()
print(games_dataframe)