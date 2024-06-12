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
        self.calculate_myelin_dmg()
        if self.health <= 0:
            self.death()

    def myelin_regeneration(self):
        if self.myelin_health < 10:
            r = random.randint(0, 100)
            if r <= self.reg_rate:
                self.myelin_health += 1
                self.tiredness += 1

    def calculate_armor(self):
        self.armor_rating = int(self.armor_rating - pow(self.tiredness/100, 2))
        if self.armor_rating < 0:
            self.armor_rating = 0
        self.armor = int(self.armor_rating * self.myelin_health)

    def calculate_myelin_dmg(self):
        ifn = self.model.IFN_matrix[self.pos[0]][self.pos[1]]
        dmg = int(ifn/100 - self.armor)
        if dmg < 0:
            dmg = 0
        if self.myelin_health < dmg:
            dmg = self.myelin_health
        self.myelin_health -= dmg
        self.MBP_release(dmg)

    def MBP_release(self, dmg):
        neighborhood = self.model.grid.get_neighborhood(self.pos, moore=True,
                                                        include_center=False)
        while dmg > 0:
            for n in neighborhood:
                self.model.MBP_matrix[n[0]][n[1]] += 1
                dmg -= 1
