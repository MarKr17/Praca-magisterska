import random
from Agents.Agent import Agent


class Neuron(Agent):

    def __init__(self, unique_id, model, reg_rate):
        super().__init__(unique_id, model)
        self.reg_rate = reg_rate
        self.health = 10
        self.myelin_health = 10
        self.current_myelin_health = 10
        self.tiredness = 0
        self.armor_rating = 10
        self.armor = self.myelin_health * self.armor_rating
        self.attached_antibodies = 0

    def step(self):
        self.myelin_regeneration()
        self.calculate_armor()
        self.antibody_attachement()
        self.calculate_myelin_dmg()
        if self.health <= 0:
            self.death()

    def myelin_regeneration(self):
        if self.current_myelin_health < 10:
            r = random.randint(0, 100)
            if r <= self.reg_rate:
                self.current_myelin_health += 1
                self.tiredness += 1

    def calculate_armor(self):
        self.armor_rating = int(self.armor_rating - pow(self.tiredness/100, 2))
        if self.armor_rating < 0:
            self.armor_rating = 0
        self.armor = int(self.armor_rating * self.current_myelin_health)

    def calculate_myelin_dmg(self):
        ifn = self.model.IFN_matrix[self.pos[0]][self.pos[1]]
        dmg = int(ifn/100 - self.armor)
        if dmg < 0:
            dmg = 0
        if self.current_myelin_health < dmg:
            dmg = self.current_myelin_health
        self.current_myelin_health -= dmg
        self.MBP_release(dmg)

    def MBP_release(self, dmg):
        neighborhood = self.model.grid.get_neighborhood(self.pos, moore=True,
                                                        include_center=False)
        while dmg > 0:
            for n in neighborhood:
                self.model.MBP_matrix[n[0]][n[1]] += 1
                dmg -= 1

    def antibody_attachement(self):
        neighborhood = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=False)
        for n in neighborhood:
            self.attached_antibodies += self.model.MBP_antibody_matrix[n[0],
                                                                       n[1]]
