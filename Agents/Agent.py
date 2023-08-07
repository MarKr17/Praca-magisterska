import mesa.agent
from mesa.model import Model


class Agent(mesa.Agent):
    def __init__(self, unique_id: int, model: Model):
        super().__init__(unique_id, model)
        self.area = 0  # value of area in which agent is located
        self.o_side = 1

    def death(self):
        self.model.kill_agents.append(self)
