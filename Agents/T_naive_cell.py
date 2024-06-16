from Agents.Cell import Cell
from Agents.Th17 import Th17
import random


class T_naive_cell(Cell):
    def __init__(self, unique_id, model, proliferation_rate):
        super().__init__(unique_id, model, proliferation_rate)
        self.antigen_attached = ''
        self.activated = False
        self.activated_proliferation_rate = int(1.5*self.proliferation_rate)
        self.differantiation_threshold = 5

    def step(self):
        self.move()
        self.activation()
        self.proliferation()
        self.differentiation()
        if self.health <= 0:
            self.death()

    def activation(self):
        if self.antigen_attached != '':
            self.activated = True
            self.proliferation_rate = self.activated_proliferation_rate

    def proliferation(self):
        r = random.randint(0, 99)
        if r < self.proliferation_rate:
            n = T_naive_cell(self.model.ID, self.model,
                             self.proliferation_rate)
            self.model.ID += 1
            self.model.new_agents.append(n)
            self.tiredness += 1

    def differentiation(self):
        r = random.randint(0, 99)
        if r < self.proliferation_rate and self.activated:
            IL6 = self.model.IL_6_matrix[self.pos[0], self.pos[1]]
            IL21 = self.model.IL_21_matrix[self.pos[0], self.pos[1]]
            if IL6 + IL21 > 5:
                n = Th17(self.model.ID, self.model,
                         self.proliferation_rate)
                self.model.ID += 1
                self.model.new_agents.append(n)
                self.tiredness += 1
