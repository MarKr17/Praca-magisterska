from mesa.model import Model
from Agents.Agent import Agent
import random


class Virus(Agent):
    def __init__(self, unique_id: int, model: Model):
        super().__init__(unique_id, model)
        self.health = 1
        self.placement = 0
        self.infection_rate = 50

    def step(self):
        self.move()
        self.cytokin_effect()
        r = random.randint(0, 99)
        if r < self.infection_rate:
            self.infect
        if self.health < 1:
            self.death()

    def move(self):
        positions = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=False)
        positions_copy = positions.copy()
        for pos in positions_copy:
            a = self.model.areas[pos[0]][pos[1]]
            if a == 1 or a == 2:
                positions.remove(pos)
        new_position = random.choice(positions)
        self.model.grid.move_agent(self, new_position)

    def death(self):
        self.model.kill_agents.append(self)

    def infect(self):
        from Agents.B_cell import B_cell
        neighbors = self.model.grid.get_neighbors(self.pos, moore=True)
        neighbors_copy = neighbors.copy()
        for n in neighbors_copy:
            if type(n) is not B_cell:
                neighbors.remove(n)
        if len(neighbors > 0):
            b = random.choice(neighbors)
            b.infected = True
            b.latency = "latency I"

    def cytokin_effect(self):
        cytokin = self.model.cytokin_matrix[self.pos[0]][self.pos[1]]
        self.health -= cytokin//10
