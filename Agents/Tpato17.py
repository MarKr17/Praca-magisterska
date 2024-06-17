from Agents.Cell import Cell
import random


class Tpato17(Cell):
    def __init__(self, unique_id, model, proliferation_rate):
        super().__init__(unique_id, model, proliferation_rate)

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
            n = Tpato17(self.model.ID, self.model,
                        self.proliferation_rate)
            self.model.ID += 1
            self.model.new_agents.append(n)
            self.tiredness += 1

    def cytokine_release(self):
        self.model.IL_17_matrix[self.pos[0], self.pos[1]] += 2
        self.tiredness += 1
