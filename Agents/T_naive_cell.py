from Agents.Cell import Cell
from Agents.Th1 import Th1
from Agents.Th17 import Th17
import random


class T_naive_cell(Cell):
    def __init__(self, unique_id, model, proliferation_rate):
        super().__init__(unique_id, model, proliferation_rate)
        self.antigen_presented = None

    def step(self):
        self.move()
        self.proliferation()
        self.differentiation()
        if self.health <= 0:
            self.death()

    def myelin_reactive_activation(self):
        if self.antigen_presented == "MBP":
            print()

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
        if r < self.proliferation_rate:
            IFN = self.model.IFN_matrix[self.pos[0], self.pos[1]]
            IL22 = self.model.IL_22_matrix[self.pos[0], self.pos[1]]
            if IFN+IL22 != 0:
                if IFN > IL22:
                    n = Th1(self.model.ID, self.model, self.proliferation_rate)
                else:
                    n = Th17(self.model.ID, self.model,
                             self.proliferation_rate)
            self.model.ID += 1
            self.model.new_agents.append(n)
            self.tiredness += 1
