from rlbot.agents.base_agent import BaseAgent
import random

class MyBot(BaseAgent):
    def initialize_agent(self):
        # Initialise ici
        self.level = 'ssl'  # Par défaut, tu peux modifier en fonction de ce que l'utilisateur choisira
        self.skills = []    # Liste des compétences à remplir (ex: ['pinch', 'flip_reset'])

    def set_parameters(self, level, skills):
        self.level = level
        self.skills = skills

    def perform_skill(self, skill_name):
        # Taux de réussite selon le niveau
        success_rate = {
            'ssl': 0.95,
            'grand_champion': 0.85,
            'diamond': 0.7,
            'platine': 0.5
        }.get(self.level.lower(), 0.5)

        if random.random() <= success_rate:
            # Compétence réussie parfaitement
            func = getattr(self, f"do_{skill_name}", None)
            if func:
                func()
            else:
                self.do_basic_move()
        else:
            # Compétence ratée partiellement ou pas du tout
            self.do_basic_move()

    def get_output(self, packet):
        # Cette fonction est appelée par RLBot à chaque frame
        # Appelle toutes les compétences cochées
        for skill in self.skills:
            self.perform_skill(skill)
        # Ici tu dois retourner un objet de commande, ex: throttle, steer...
        # Simplifié pour l'exemple
        return self.quick_output(packet)

    def quick_output(self, packet):
        # Exemple basique de sortie (avancer droit)
        from rlbot.utils.structures.quick_chats import QuickChats
        controls = self.agent_input()
        controls.throttle = 1.0
        controls.steer = 0.0
        return controls

    def do_pinch(self):
        print("Exécution du Pinch")

    def do_ground_pinch(self):
        print("Exécution du Ground Pinch")

    def do_cuxir_pinch(self):
        print("Exécution du Cuxir Pinch")

    def do_flip_reset(self):
        print("Exécution du Flip Reset")

    def do_multiple_flip_resets(self):
        print("Exécution du Multiple Flip Resets")

    def do_flip_reset_musty(self):
        print("Exécution du Flip Reset Musty")

    def do_flip_reset_breezi(self):
        print("Exécution du Flip Reset Breezi")

    def do_ceiling_reset(self):
        print("Exécution du Ceiling Reset")

    def do_no_flip_shot(self):
        print("Exécution du No Flip Shot")

    def do_delayed_flip_shot(self):
        print("Exécution du Delayed Flip Shot")

    # Ajoute les autres compétences ici...

    def do_speed_flip(self):
        print("Exécution du Speed Flip")

    def do_flip_chain(self):
        print("Exécution du Flip Chain")

    def do_infield_pass(self):
        print("Exécution du Infield Pass")

    def do_backboard_pass(self):
        print("Exécution du Backboard Pass")

    def do_shadow_defense(self):
        print("Exécution du Shadow Defense")

    def do_passing_plays(self):
        print("Exécution du Passing Plays")

    def do_bumps_demos(self):
        print("Exécution du Bumps & Demos")

    def do_rotation(self):
        print("Exécution du Rotation")

    def do_basic_move(self):
        print("Exécution d'un mouvement basique")

