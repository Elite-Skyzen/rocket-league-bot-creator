<<<<<<< HEAD
import subprocess

def prepare_match(form_data):
    # Lancer RLBot
    try:
        subprocess.Popen(["rlbot"])
    except Exception as e:
        print(f"Erreur lors du lancement de RLBot : {e}")
import subprocess

def prepare_match(form_data):
    # Lancer RLBot
    try:
        subprocess.Popen(["rlbot"])
    except Exception as e:
        print(f"Erreur lors du lancement de RLBot : {e}")
import subprocess

def prepare_match(data):
    config_path = 'match_config.cfg'
    with open(config_path, 'w') as f:
        f.write(f"arena = {data['arena']}\n")
        f.write(f"mode = {data['mode']}\n")
        f.write(f"mutators = {data['mutators']}\n")
        f.write(f"bot = {data['bot_name']}\n")

    # Exemple : lancement de RLBot
    try:
        subprocess.Popen(["rlbot", "--config", config_path])
    except FileNotFoundError:
        print("❌ RLBot non trouvé. Installe RLBot avec pip install rlbot")

import json
import json
from rlbot.setup_manager import SetupManager
from rlbot.matchconfig.match_config import MatchConfig, PlayerConfig, Team
from rlbot.parsing.bot_config_bundle import BotConfigBundle
from rlbot.utils.logging_utils import get_logger
import os

logger = get_logger("MatchLauncher")

def prepare_match(bot_name, car, difficulty, rank, mode, arena, mutators, skills):
    match_config = MatchConfig()
    match_config.game_mode = "Soccar"
    match_config.game_map = arena
    match_config.player_configurations = []

    # Crée le fichier de config JSON
    bot_config_data = {
        "name": bot_name,
        "car": car,
        "difficulty": difficulty,
        "rank": rank,
        "skills": skills,
        "mutators": mutators
    }

    with open("bot_config.json", "w") as f:
        json.dump(bot_config_data, f)

    # Charge ton bot RLBot avec ce fichier
    player = PlayerConfig()
    player.bot = True
    player.name = bot_name
    player.rlbot_config_path = os.path.abspath("bot.cfg")  # ← à adapter si ton bot est ailleurs
    player.team = 0

    match_config.player_configurations.append(player)

    # Ajouter un bot de l'équipe adverse pour test ?
    opponent = PlayerConfig()
    opponent.bot = False
    opponent.name = "Joueur Humain"
    opponent.team = 1
    match_config.player_configurations.append(opponent)

    setup_manager = SetupManager()
    setup_manager.load_match_config(match_config)
    setup_manager.launch_bot_processes()
    setup_manager.start_match()

def prepare_match(data):
    with open("match_config.json", "w") as f:
        json.dump(data, f, indent=2)
=======
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
>>>>>>> a43cee6bf72974d7ef337ade287be5a84cf45d1e
