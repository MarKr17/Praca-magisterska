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
        self.viral_replication_rate = self.model.Proliferation_rate["Virus"]
        self.activated_proliferation_rate = self.proliferation_rate*2

    def step(self):
        self.move()
        self.activation()
        self.infection_switch()
        r = random.randint(0, 99)
        if self.infection_state == "lytic" and r < self.viral_replication_rate:
            self.viral_replication()
            self.health = 0
        elif r < self.proliferation_rate:
            if self.activated is True:
                self.differentiation()
            else:
                self.proliferation()
        self.calculate_dmg()
        if self.health <= 0:
            self.death()

    def viral_replication(self):
        from Agents.Virus import Virus
        neighborhood = self.model.grid.get_neighborhood(self.pos, moore=True,
                                                        include_center=False,
                                                        radius=3)
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
        n.infection("latent")
        n.antigen_presented = self.antigen_presented
        n.pos = self.child_pos()
        n.calculate_side()
        self.model.ID += 1
        self.model.new_agents.append(n)
        self.tiredness += 1

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
                self.proliferation_rate = self.activated_proliferation_rate
            else:
                IL21 = self.model.IL_21_matrix[self.pos[0], self.pos[1]]
                if IL21 >= self.cytokine_activation_threshold:
                    self.activated = True
                    self.proliferation_rate = self.activated_proliferation_rate

    def infection_switch(self):
        if self.infection_state == "latent":
            TGF = self.model.TGF_matrix[self.pos[0], self.pos[1]]
            self.health = self.health * 2
            if TGF >= self.lytic_threshold:
                self.infection_state = "lytic"

    def infection(self, state):
        if state == "latent":
            self.infection_state = "latent"
            self.health = int(self.health * 1.5)
            self.dmg_factor = self.dmg_factor * 1
            self.proliferation_rate = self.proliferation_rate
