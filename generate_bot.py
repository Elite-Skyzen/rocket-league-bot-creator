import os
<<<<<<< HEAD
import json

def create_bot_zip(form_data):
    bot_name = form_data['bot_name']

    # Définir les compétences sélectionnées
    selected_skills = form_data.get('skills', [])

    # Créer le fichier settings.json
    settings = {
        "bot_name": bot_name,
        "difficulty": form_data['rank'],
        "skills": selected_skills
    }

    with open('settings.json', 'w') as f:
        json.dump(settings, f, indent=4)

    return "Bot ready"

=======
import zipfile
import json

def create_bot_zip(data):
    bot_name = data.get('bot_name', 'CustomBot')
    car = data.get('car', 'Octane')
    difficulty = data.get('difficulty', 'moyen')
    rank = data.get('rank', 'platine')

    folder = f"bots/{bot_name}"
    os.makedirs(folder, exist_ok=True)

    with open(os.path.join(folder, f"{bot_name}.py"), 'w') as f:
        f.write(f'''
from rlbot.agents.base_agent import BaseAgent, SimpleControllerState

class {bot_name}(BaseAgent):
    def get_output(self, packet):
        return SimpleControllerState(throttle=1.0)
''')

    with open(os.path.join(folder, 'bot.cfg'), 'w') as f:
        f.write(f'''[RLBot]
bot_class_path = {bot_name}.{bot_name}
name = {bot_name}
team = 0
''')

    settings = {
        "rocket_league_path": "C:/Program Files/Epic Games/RocketLeague/Binaries/Win64/RocketLeague.exe",
        "bot_name": bot_name,
        "bot_difficulty": difficulty,
        "bot_car": car,
        "bot_rank": rank
    }

    with open(os.path.join(folder, 'settings.json'), 'w') as f:
        json.dump(settings, f, indent=2)

    zip_path = f"{folder}.zip"
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for root, _, files in os.walk(folder):
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, folder)
                zipf.write(full_path, arcname=rel_path)

    return zip_path
>>>>>>> a43cee6bf72974d7ef337ade287be5a84cf45d1e
