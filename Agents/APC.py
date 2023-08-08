from Agents.Cell import Cell
import random


class APC(Cell):
    def __init__(self, unique_id, model, proliferation_rate):
        super().__init__(unique_id, model, proliferation_rate)
        self.MHC_grow_rate = 5
        self.num_MHC = 0

    def step(self):
        self.move()
        self.proliferation()
        if self.health <= 0:
            self.death

    def grow_MHC(self):
        r = random.randint(0, 99)
        if r < self.MHC_grow_rate:
            self.num_MHC += 1
