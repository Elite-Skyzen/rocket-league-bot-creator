import os
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

