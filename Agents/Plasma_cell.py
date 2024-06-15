from Agents.Cell import Cell
import random


class Plasma_cell(Cell):
    def __init__(self, unique_id, model, proliferation_rate):
        super().__init__(unique_id, model, proliferation_rate)
        self.antigen_presented = ''
        self.antibody_production_rate = 0

    def step(self):
        self.move()
        self.proliferation()
        if self.antigen_presented != '':
            self.antibody_production()
        if self.health <= 0:
            self.death()

    def proliferation(self):
        r = random.randint(0, 99)
        if r < self.proliferation_rate:
            n = Plasma_cell(self.model.ID, self.model, self.proliferation_rate)
            self.model.ID += 1
            self.model.new_agents.append(n)
            self.tiredness += 1

    def antibody_production(self):
        r = random.randint(0, 99)
        if r < self.antibody_production_rate:
            x = self.pos[0]
            y = self.pos[1]
            if self.antigen_presented == "MBP":
                self.model.MBP_antibody_matrix[x][y] += 1
            if self.antigen_presented == "EBNA1":
                self.model.EBNA1_antibody_matrix[x][y] += 1
            self.tiredness += 1
