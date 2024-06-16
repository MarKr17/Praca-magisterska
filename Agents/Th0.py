from Agents.Cell import Cell
from Agents.Th2 import Th2
import random


class Th0(Cell):
    def __init__(self, unique_id, model, proliferation_rate):
        super().__init__(unique_id, model, proliferation_rate)
        self.antigen_attached = ''

    def step(self):
        self.move()
        self.cytokine_release()
        self.proliferation()
        self.differentiation()
        if self.health <= 0:
            self.death()

    def proliferation(self):
        r = random.randint(0, 99)
        if r < self.proliferation_rate:
            n = Th0(self.model.ID, self.model,
                    self.proliferation_rate)
            self.model.ID += 1
            self.model.new_agents.append(n)
            self.tiredness += 1

    def cytokine_release(self):
        self.model.IL_2_matrix[self.pos[0], self.pos[1]] += 2
        self.model.IL_4_matrix[self.pos[0], self.pos[1]] += 2
        self.model.IFN_matrix[self.pos[0], self.pos[1]] += 2

    def differentiation(self):
        r = random.randint(0, 99)
        IL4 = self.model.IL_4_matrix[self.pos[0], self.pos[1]]
        IFN = self.model.IFN_matrix[self.pos[0], self.pos[1]]
        if r < self.proliferation_rate:
            if IL4 > IFN:
                n = Th2(self.model.ID, self.model,
                        self.proliferation_rate)
            self.model.ID += 1
            self.model.new_agents.append(n)
            self.tiredness += 1