from Agents.Cell import Cell
import random


class Plasma_cell(Cell):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.antigen_presented = ''
        self.antibody_production_rate = 50
        self.proliferation_rate = int(self.model.Proliferation_rate["B-cell"]
                                      / 2)
        self.health = self.model.Health["B-cell"]
        self.dmg_factor = self.model.Dmg_factor["B-cell"]

    def step(self):
        self.move()
        r = random.randint(0, 100)
        if r < self.proliferation_rate:
            self.proliferation()
        if self.antigen_presented != '' and r < self.antibody_production_rate:
            self.antibody_production()
        self.calculate_dmg()
        if self.health <= 0:
            self.death()

    def proliferation(self):
        n = Plasma_cell(self.model.ID, self.model)
        n.pos = self.child_pos()
        n.calculate_side()
        self.model.ID += 1
        self.model.new_agents.append(n)
        self.tiredness += 1

    def antibody_production(self):
        x = self.pos[0]
        y = self.pos[1]
        if self.antigen_presented == "MBP":
            self.model.MBP_antibody_matrix[x][y] += 20
        if self.antigen_presented == "EBNA1":
            self.model.EBNA1_antibody_matrix[x][y] += 20
        self.tiredness += 1
