from Agents.Cell import Cell
from Agents.Th0 import Th0
import random


class Th_cell(Cell):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.antigen_presented = ''
        self.activated = False
        self.proliferation_rate = self.model.Proliferation_rate["T-cell"]
        self.health = self.model.Health["T-cell"]
        self.dmg_factor = self.model.Dmg_factor["T-cell"]
        self.activated_proliferation_rate = int(1.5*self.proliferation_rate)
        self.reactive_to = "EBNA1"

    def step(self):
        self.move()
        self.activation()
        self.cytokine_release()
        r = random.randint(0, 99)
        if r < self.proliferation_rate:
            IL2 = self.model.IL_2_matrix[self.pos[0], self.pos[1]]
            if IL2 > 0:
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

    def proliferation(self):
        n = Th_cell(self.model.ID, self.model)
        n.pos = self.child_pos()
        n.calculate_side()
        n.reactive_to = self.reactive_to
        self.model.ID += 1
        self.model.new_agents.append(n)
        self.tiredness += 1

    def cytokine_release(self):
        if self.activated:
            self.model.IL_2_matrix[self.pos[0], self.pos[1]] += 1
            self.tiredness += 1

    def differentiation(self):
        n = Th0(self.model.ID, self.model)
        n.pos = self.child_pos()
        n.calculate_side()
        n.reactive_to = self.reactive_to
        self.model.ID += 1
        self.model.new_agents.append(n)
        self.tiredness += 1
