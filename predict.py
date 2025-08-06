def predict_match(home_team, away_team):
    # Dummy prediction logic (replace this later with real data model)
    home_score = len(home_team) % 5 + 1
    away_score = len(away_team) % 4 + 1

    result = {
        "Home Win Probability": f"{round(50 + (home_score - away_score) * 5, 1)}%",
        "Away Win Probability": f"{round(50 - (home_score - away_score) * 5, 1)}%",
        "Predicted Home Goals": home_score,
        "Predicted Away Goals": away_score,
        "Expected Total Goals": home_score + away_score,
        "Over 2.5 Goals": "Yes" if home_score + away_score > 2.5 else "No"
    }

    return result
