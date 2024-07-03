from Agents.Cell import Cell
import random


class Th2(Cell):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.proliferation_rate = self.model.Proliferation_rate["T-cell"]
        self.health = self.model.Health["T-cell"]
        self.dmg_factor = self.model.Dmg_factor["T-cell"]
        self.reactive_to = "EBNA1"
        self.MBP_exposure = 0

    def step(self):
        self.move()
        self.cytokine_release()
        self.proliferation()
        self.calculate_dmg()
        if self.health <= 0:
            self.death()

    def proliferation(self):
        r = random.randint(0, 99)
        if r < self.proliferation_rate:
            n = Th2(self.model.ID, self.model)
            self.model.ID += 1
            n.pos = self.child_pos()
            n.calculate_side()
            n.reactive_to = self.reactive_to
            self.model.new_agents.append(n)
            self.tiredness += 1

    def cytokine_release(self):
        self.model.IL_4_matrix[self.pos[0], self.pos[1]] += 1
        self.model.IL_6_matrix[self.pos[0], self.pos[1]] += 1
        self.tiredness += 1
