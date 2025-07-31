from rlbot.setup_manager import SetupManager

def prepare_match(form_data):
    setup = SetupManager()
    setup.set_match_config(
        team_size=1,
        match_length=5,
        arena=form_data['arena'],
        game_mode=form_data['mode'],
        mutators=form_data['mutators'],
    )

    # Ajout du bot créé
    setup.add_bot(
        name=form_data['bot_name'],
        bot_path=f"bots/{form_data['bot_name']}/{form_data['bot_name']}.py",
        team=0,
        car_name=form_data['car'],
        difficulty=form_data['difficulty']
    )
    # Lancer le match
    setup.launch_match()
