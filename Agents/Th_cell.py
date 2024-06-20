from Agents.Cell import Cell
from Agents.Th0 import Th0
import random


class Th_cell(Cell):
    def __init__(self, unique_id, model, proliferation_rate):
        super().__init__(unique_id, model, proliferation_rate)
        self.antigen_presented = ''
        self.activated = False
        self.health = 15
        self.activated_proliferation_rate = int(1.5*self.proliferation_rate)

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
        if self.antigen_presented != '':
            self.activated = True
            self.proliferation_rate = self.activated_proliferation_rate

    def proliferation(self):
        n = Th_cell(self.model.ID, self.model,
                    self.proliferation_rate)
        self.model.ID += 1
        self.model.new_agents.append(n)
        self.tiredness += 1

    def cytokine_release(self):
        if self.activated:
            self.model.IL_2_matrix[self.pos[0], self.pos[1]] += 1
            self.tiredness += 1

    def differentiation(self):
        n = Th0(self.model.ID, self.model,
                self.proliferation_rate)
        self.model.ID += 1
        self.model.new_agents.append(n)
        self.tiredness += 1
