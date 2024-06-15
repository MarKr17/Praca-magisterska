from Agents.Cell import Cell
from Agents.Plasma_cell import Plasma_cell
import random


class B_cell(Cell):
    def __init__(self, unique_id, model, proliferation_rate):
        super().__init__(unique_id, model, proliferation_rate)
        self.infection_state = ""
        self.activated = False
        self.proteins = []
        self.antigen_presented = ''

    def step(self):
        self.move()
        if self.infection_state == "lytic":
            self.viral_replication()
            self.health = 0
        else:
            if self.activated is True:
                self.differentiation()
            else:
                self.proliferation()
        if self.health <= 0:
            self.death()

    def viral_replication(self):
        from Agents.Virus import Virus
        neighborhood = self.model.grid.get_neighborhood(self.pos, moore=True,
                                                        include_center=False)
        neighborhood_copy = neighborhood.copy()
        for n in neighborhood_copy:
            a = self.model.areas[n[0]][n[1]]
            if a == 1:
                neighborhood.remove(n)
        for n in neighborhood:
            v = Virus(self.model.ID, self.model)
            self.model.ID += 1
            self.model.new_agents.append(v)
            self.tiredness += 1
        self.infection_state = "latent"

    def proliferation(self):
        r = random.randint(0, 99)
        if r < self.proliferation_rate:
            n = B_cell(self.model.ID, self.model, self.proliferation_rate)
            n.infectrion_state = self.infection_state
            self.model.ID += 1
            self.model.new_agents.append(n)
            self.tiredness += 1

    def differentiation(self):
        r = random.randint(0, 99)
        if r < self.proliferation_rate:
            n = Plasma_cell(self.model.ID, self.model, self.proliferation_rate)
            self.model.ID += 1
            self.model.new_agents.append(n)
            self.tiredness += 1
