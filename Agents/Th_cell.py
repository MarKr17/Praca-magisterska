from Agents.Cell import Cell
from Agents.Th0 import Th0
import random


class Th_cell(Cell):
    def __init__(self, unique_id, model, proliferation_rate):
        super().__init__(unique_id, model, proliferation_rate)
        self.antigen_attached = ''
        self.activated = False
        self.activated_proliferation_rate = int(1.5*self.proliferation_rate)

    def step(self):
        self.move()
        self.activation()
        self.cytokine_release()
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
            n = Th_cell(self.model.ID, self.model,
                        self.proliferation_rate)
            self.model.ID += 1
            self.model.new_agents.append(n)
            self.tiredness += 1

    def cytokine_release(self):
        if self.activated:
            self.model.IL_2_matrix[self.pos[0], self.pos[1]] += 2

    def differentiation(self):
        r = random.randint(0, 99)
        IL2 = self.model.IL_2_matrix[self.pos[0], self.pos[1]]
        if r < self.proliferation_rate and IL2 > 0:
            n = Th0(self.model.ID, self.model,
                    self.proliferation_rate)
            self.model.ID += 1
            self.model.new_agents.append(n)
            self.tiredness += 1
