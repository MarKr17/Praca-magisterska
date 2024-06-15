from Agents.Cell import Cell
from Agents.B_cell import B_cell
from Agents.Plasma_cell import Plasma_cell
import random


class APC(Cell):
    def __init__(self, unique_id, model, proliferation_rate):
        super().__init__(unique_id, model, proliferation_rate)
        self.MHC_grow_rate = 5
        self.num_MHC = 0
        self.antigen_attached = ''

    def step(self):
        self.move()
        self.proliferation()
        if self.antigen_attached != '':
            self.antigen_attachment()
        if self.health <= 0:
            self.death

    def grow_MHC(self):
        r = random.randint(0, 99)
        if r < self.MHC_grow_rate:
            self.num_MHC += 1

    def antigen_attachment(self):
        MBP = self.model.MBP_matrix[self.pos[0], self.pos[1]]
        EBNA1 = self.model.EBNA1_matrix[self.pos[0], self.pos[1]]
        if MBP + EBNA1 != 0:
            if MBP > EBNA1:
                self.antigen_attached = "MBP"
                self.model.MBP_matrix[self.pos[0], self.pos[1]] -= 1
            else:
                self.antigen_attached = "EBNA1"
                self.model.EBNA1_matrix[self.pos[0], self.pos[1]] -= 1

    def antigen_presentation(self):
        neighbors = self.model.grid.get_neighbors(self.pos, moore=True)
        neighbors_copy = neighbors.copy()
        for n in neighbors_copy:
            if isinstance(n, (B_cell, Plasma_cell)):
                neighbors.remove(n)
        if len(neighbors) > 0:
            b = random.choice(neighbors)
            b.antigen_presented = self.antigen_attached
            self.antigen_attached = ''
