from Agents.Cell import Cell
from Agents.Plasma_cell import Plasma_cell
import random


class B_cell(Cell):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.infection_state = ""
        self.activated = False
        self.proteins = []
        self.antigen_presented = ''
        self.cytokine_activation_threshold = 5
        self.lytic_threshold = 5
        self.proliferation_rate = self.model.Proliferation_rate["B-cell"]
        self.health = self.model.Health["B-cell"]
        self.dmg_factor = self.model.Dmg_factor["B-cell"]

    def step(self):
        self.move()
        self.activation()
        self.infection_switch()
        r = random.randint(0, 99)
        if r < self.proliferation_rate:
            if self.infection_state == "lytic":
                self.viral_replication()
                self.health = 0
            elif self.activated is True:
                self.differentiation()
            else:
                self.proliferation()
        self.calculate_dmg()
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
            v.pos = n
            self.model.ID += 1
            self.model.new_agents.append(v)
            self.tiredness += 1
        self.tiredness += 1

    def proliferation(self):
        n = B_cell(self.model.ID, self.model)
        n.infectrion_state = self.infection_state
        n.antigen_presented = self.antigen_presented
        n.pos = self.child_pos()
        n.calculate_side()
        self.model.ID += 1
        self.model.new_agents.append(n)
        self.tiredness += 2

    def differentiation(self):
        n = Plasma_cell(self.model.ID, self.model)
        n.pos = self.child_pos()
        n.calculate_side()
        self.model.ID += 1
        self.model.new_agents.append(n)
        self.tiredness += 1

    def activation(self):
        if self.infection_state != "lytic":
            if self.antigen_presented != '':
                self.activated = True
            else:
                IL21 = self.model.IL_21_matrix[self.pos[0], self.pos[1]]
                if IL21 >= self.cytokine_activation_threshold:
                    self.activated = True

    def infection_switch(self):
        if self.infection_state == "latent":
            TGF = self.model.TGF_matrix[self.pos[0], self.pos[1]]
            if TGF >= self.lytic_threshold:
                self.infection_state = "lytic"
