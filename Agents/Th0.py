from Agents.Cell import Cell
from Agents.Th2 import Th2
from Agents.Th1 import Th1
import random


class Th0(Cell):
    def __init__(self, unique_id, model, proliferation_rate):
        super().__init__(unique_id, model, proliferation_rate)
        self.antigen_presented = ''
        self.health = 10

    def step(self):
        self.move()
        self.cytokine_release()
        r = random.randint(0, 99)
        if r < self.proliferation_rate:
            IL4 = self.model.IL_4_matrix[self.pos[0], self.pos[1]]
            IFN = self.model.IFN_matrix[self.pos[0], self.pos[1]]
            if IL4 + IFN > 0:
                self.differentiation(IL4, IFN)
            else:
                self.proliferation()
        self.calculate_dmg()
        if self.health <= 0:
            self.death()

    def proliferation(self):
        n = Th0(self.model.ID, self.model,
                self.proliferation_rate)
        self.model.ID += 1
        self.model.new_agents.append(n)
        self.tiredness += 2

    def cytokine_release(self):
        self.model.IL_2_matrix[self.pos[0], self.pos[1]] += 1
        self.model.IL_4_matrix[self.pos[0], self.pos[1]] += 1
        self.model.IFN_matrix[self.pos[0], self.pos[1]] += 1
        self.tiredness += 1

    def differentiation(self, IL4, IFN):
        if IL4 > IFN:
            n = Th2(self.model.ID, self.model,
                    self.proliferation_rate)
        else:
            n = Th1(self.model.ID, self.model,
                    self.proliferation_rate)
        self.model.ID += 1
        self.model.new_agents.append(n)
        self.tiredness += 1
