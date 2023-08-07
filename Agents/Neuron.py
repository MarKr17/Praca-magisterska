import random
from Agents.Agent import Agent


class Neuron(Agent):

    def __init__(self, unique_id, model, reg_rate):
        super().__init__(unique_id, model)
        self.reg_rate = reg_rate
        self.health = 10
        self.myelin_health = 10
        self.tiredness = 0
        self.armor_rating = 10
        self.armor = self.myelin_health * self.armor_rating

    def step(self):
        self.myelin_regeneration()
        self.calculate_armor()
        if self.health <= 0:
            self.death()

    def myelin_regeneration(self):
        if self.myelin_health < 10:
            r = random.randint(0, 100)
            if r <= self.reg_rate:
                self.myelin_health += 1
                self.tiredness += 1

    def calculate_armor(self):
        self.armor_rating = self.armor_rating - pow(self.tiredness/10, 2)
        self.armor = self.armor_rating * self.myelin_health
