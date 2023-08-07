from Agents.Cell import Cell
import random


class T_cell(Cell):
    def __init__(self, unique_id, model, proliferation_rate, cytokin_rate):
        super().__init__(unique_id, model, proliferation_rate)
        self.cytokine_rate = cytokin_rate

    def step(self):
        self.move()
        self.cytokine_release()
        self.proliferation()
        if self.health <= 0:
            self.death()

    def cytokine_release(self):
        r = random.randint(0, 99)
        if r < self.cytokine_rate:
            x = self.pos[0]
            y = self.pos[1]
            self.model.cytokine_matrix[x][y] += 1
            self.tiredness += 1
