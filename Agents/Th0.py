from Agents.Cell import Cell
from Agents.Th2 import Th2
from Agents.Th1 import Th1
import random


class Th0(Cell):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.antigen_presented = ''
        self.proliferation_rate = self.model.Proliferation_rate["Th-cell"]
        self.health = self.model.Health["Th-cell"]
        self.dmg_factor = self.model.Dmg_factor["Th-cell"]
        self.reactive_to = ["EBNA1"]
        self.cytokine_threshold = 2
        self.MBP_exposure = 0

    def step(self):
        self.move()
        self.cytokine_release()
        r = random.randint(0, 99)
        if r < self.proliferation_rate:
            IL4 = self.model.IL_4_matrix[self.pos[0], self.pos[1]]
            IFN = self.model.IFN_matrix[self.pos[0], self.pos[1]]
            if IL4 + IFN > self.cytokine_threshold:
                self.differentiation(IL4, IFN)
            else:
                self.proliferation()
        self.calculate_dmg()
        if self.health <= 0:
            self.death()

    def proliferation(self):
        n = Th0(self.model.ID, self.model)
        n.pos = self.child_pos()
        n.calculate_side()
        n.reactive_to = self.reactive_to
        self.model.ID += 1
        self.model.new_agents.append(n)
        self.tiredness += 1

    def cytokine_release(self):
        self.model.IL_2_matrix[self.pos[0],
                               self.pos[1]] += self.model.cytokine_amount
        self.model.IL_4_matrix[self.pos[0],
                               self.pos[1]] += self.model.cytokine_amount
        self.model.IFN_matrix[self.pos[0],
                              self.pos[1]] += self.model.cytokine_amount
        self.tiredness += 1

    def differentiation(self, IL4, IFN):
        if IL4 > IFN:
            n = Th2(self.model.ID, self.model)
        else:
            n = Th1(self.model.ID, self.model)
        n.pos = self.child_pos()
        n.calculate_side()
        n.reactive_to = self.reactive_to
        self.model.ID += 1
        self.model.new_agents.append(n)
        self.tiredness += 1
