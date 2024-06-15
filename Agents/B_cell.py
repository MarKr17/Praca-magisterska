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
        self.cytokine_activation_threshold = 5

    def step(self):
        self.move()
        self.activation()
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
            n.antigen_presented = self.antigen_presented
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

    def activation(self):
        if self.infection_state != "lytic":
            if self.antigen_presented != '':
                self.activated = True
            else:
                IL22 = self.model.IL_22_matrix[self.pos[0], self.pos[1]]
                if IL22 >= self.cytokine_activation_threshold:
                    self.activated = True
