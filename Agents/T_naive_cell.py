from Agents.Cell import Cell
from Agents.Treg17 import Treg17
from Agents.Tpato17 import Tpato17
import random


class T_naive_cell(Cell):
    def __init__(self, unique_id, model, proliferation_rate):
        super().__init__(unique_id, model, proliferation_rate)
        self.antigen_presented = ''
        self.health = 10
        self.activated = False
        self.activated_proliferation_rate = int(1.5*self.proliferation_rate)

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
        if self.antigen_presented != '':
            self.activated = True
            self.proliferation_rate = self.activated_proliferation_rate

    def proliferation(self):
        n = T_naive_cell(self.model.ID, self.model,
                         self.proliferation_rate)
        self.model.ID += 1
        self.model.new_agents.append(n)
        self.tiredness += 2

    def differentiation(self):
        IL6 = self.model.IL_6_matrix[self.pos[0], self.pos[1]]
        TGF = self.model.TGF_matrix[self.pos[0], self.pos[1]]

        IL21 = self.model.IL_21_matrix[self.pos[0], self.pos[1]]
        TNF = self.model.TNF_matrix[self.pos[0], self.pos[1]]

        if IL6 + TGF > IL21 + TNF:
            n = Treg17(self.model.ID, self.model,
                       self.proliferation_rate)
        else:
            n = Tpato17(self.model.ID, self.model,
                        self.proliferation_rate)
        self.model.ID += 1
        self.model.new_agents.append(n)
        self.tiredness += 1
