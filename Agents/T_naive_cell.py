from Agents.Cell import Cell
from Agents.Treg17 import Treg17
from Agents.Tpato17 import Tpato17
import random


class T_naive_cell(Cell):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.antigen_presented = ''
        self.proliferation_rate = self.model.Proliferation_rate["T-cell"]
        self.health = self.model.Health["T-cell"]
        self.dmg_factor = self.model.Dmg_factor["T-cell"]
        self.activated = False
        self.activated_proliferation_rate = int(self.proliferation_rate)*2
        self.reactive_to = "EBNA1"
        self.cytokine_threshold = 10
        self.MBP_exposure = 0

    def step(self):
        self.move()
        self.activation()
        r = random.randint(0, 99)
        if r < self.proliferation_rate:
            if self.activated:
                self.differentiation()
            else:
                self.proliferation()
        self.calculate_dmg()
        if self.health <= 0:
            self.death()

    def activation(self):
        if self.antigen_presented in self.reactive_to:
            self.activated = True
            self.proliferation_rate = self.activated_proliferation_rate
        elif (self.model.hypothesis == "Bystander activation" and
              self.reactive_to == "MBP"):
            if self.model.cytokin_matrix[self.pos] >= self.cytokine_threshold:
                self.activated = True
                self.proliferation_rate = self.activated_proliferation_rate
        elif (self.model.hypothesis == "Epitope spreading" and
              self.antigen_presented == 'MBP'):
            r = random.randint(0, 99)
            if r < self.MBP_exposure:
                self.activated = True
                self.proliferation_rate = self.activated_proliferation_rate

    def proliferation(self):
        n = T_naive_cell(self.model.ID, self.model)
        n.pos = self.child_pos()
        n.calculate_side()
        n.reactive_to = self.reactive_to
        self.model.ID += 1
        self.model.new_agents.append(n)
        self.tiredness += 1

    def differentiation(self):
        IL6 = self.model.IL_6_matrix[self.pos[0], self.pos[1]]
        TGF = self.model.TGF_matrix[self.pos[0], self.pos[1]]

        IL21 = self.model.IL_21_matrix[self.pos[0], self.pos[1]]

        if IL6 + TGF > IL21*1.5:
            n = Treg17(self.model.ID, self.model)
        else:
            n = Tpato17(self.model.ID, self.model)
        n.pos = self.child_pos()
        n.calculate_side()
        n.reactive_to = self.reactive_to
        self.model.ID += 1
        self.model.new_agents.append(n)
        self.tiredness += 1
