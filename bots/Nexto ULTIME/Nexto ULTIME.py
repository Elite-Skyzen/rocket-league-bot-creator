
from rlbot.agents.base_agent import BaseAgent, SimpleControllerState

class Nexto ULTIME(BaseAgent):
    def get_output(self, packet):
        return SimpleControllerState(throttle=1.0)
