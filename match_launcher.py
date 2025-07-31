import json
import os

def prepare_match(data):
    settings = {
        "rocket_league_path": "C:/Program Files/Epic Games/RocketLeague/Binaries/Win64/RocketLeague.exe",
        "bot_name": data.get('bot_name', 'CustomBot'),
        "bot_difficulty": data.get('difficulty', 'moyen'),
        "bot_car": data.get('car', 'Octane'),
        "bot_rank": data.get('rank', 'platine'),
        "mode": data.get('mode', '1v1'),
        "arena": data.get('arena', 'DFH Stadium'),
        "mutators": data.get('mutators', 'default')
    }

    os.makedirs("match", exist_ok=True)

    with open("match/settings.json", "w") as f:
        json.dump(settings, f, indent=2)

    print("✅ Match prêt avec les paramètres :", settings)
