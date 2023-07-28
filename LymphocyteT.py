from Lymphocyte import Lymphocyte
import random


class LymphocyteT(Lymphocyte):
    def __init__(self, unique_id, model, cytokin_rate):
        super().__init__(unique_id, model)
        self.cytokine_rate = cytokin_rate

    def step(self):
        self.move()
        self.cytokine_release()

    def cytokine_release(self):
        r = random.randint(0, 100)
        if r <= self.cytokine_rate:
            x = self.pos[0]
            y = self.pos[1]
            self.model.cytokine_matrix[x][y] += 1
