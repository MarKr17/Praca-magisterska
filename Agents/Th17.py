from Agents.Cell import Cell
import random


class Th17(Cell):
    def __init__(self, unique_id, model, proliferation_rate, cytokin_rate):
        super().__init__(unique_id, model, proliferation_rate)
        self.cytokin_rate = cytokin_rate
        self.activated = False
        self.antigen_attached = ''
        self.activated_proliferation_rate = int(1.5 * self.proliferation_rate)

    def step(self):
        self.move()
        self.activation()
        if self.activated:
            self.cytokine_release()
        self.proliferation()
        if self.health <= 0:
            self.death()

    def cytokine_release(self):
        r = random.randint(0, 99)
        if r < self.cytokin_rate and self.activated is True:
            x = self.pos[0]
            y = self.pos[1]
            self.model.cytokine_matrix[x][y] += 1
            self.tiredness += 1

    def activation(self):
        if self.antigen_attached != '':
            self.activated = True
            self.proliferation_rate = self.activated_proliferation_rate
