from mesa.model import Model
from Agents.Agent import Agent
import random


class Virus(Agent):
    def __init__(self, unique_id: int, model: Model):
        super().__init__(unique_id, model)
        self.health = 1
        self.placement = 0
        self.infection_rate = 50
        self.current_infection_rate = 50
        self.attached_antibodies = 0

    def step(self):
        self.move()
        self.cytokin_effect()
        self.antibody_attachement()
        r = random.randint(0, 99)
        if r < self.current_infection_rate:
            self.infect()
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
        self.EBNA1_release

    def infect(self):
        from Agents.B_cell import B_cell
        neighbors = self.model.grid.get_neighbors(self.pos, moore=True)
        neighbors_copy = neighbors.copy()
        for n in neighbors_copy:
            if type(n) is not B_cell:
                neighbors.remove(n)
        if len(neighbors) > 0:
            b = random.choice(neighbors)
            b.infection_state = "lytic"

    def cytokin_effect(self):
        cytokin = self.model.cytokin_matrix[self.pos[0]][self.pos[1]]
        self.health -= cytokin//10

    def antibody_attachement(self):
        neighborhood = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=False)
        for n in neighborhood:
            self.attached_antibodies += self.model.EBNA1_antibody_matrix[n[0],
                                                                         n[1]]
        x = int(self.infection_rate * 0.1 * self.attached_antibodies)
        self.current_infection_rate = self.infection_rate - x
        if self.current_infection_rate < 0:
            self.current_infection_rate = 0

    def EBNA1_release(self):
        neighborhood = self.model.grid.get_neighborhood(self.pos, moore=True)
        for n in neighborhood:
            self.model.MBP_matrix[n[0]][n[1]] += 1
