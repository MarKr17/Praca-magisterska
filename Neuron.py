import mesa
import random


class Neuron(mesa.Agent):

    def __init__(self, unique_id, model, reg_rate):
        super().__init__(unique_id, model)
        self.reg_rate = reg_rate
        self.health = 1
        self.myelin_health = 10

    def step(self):
        if self.health <= 0:
            self.death()

    def death(self):
        self.model.kill_agents.append(self)

    def myelin_regeneration(self):
        if self.myelin_health < 10:
            r = random.randint(1, 100)
            if r <= self.reg_rate:
                self.myelin_health += 1
