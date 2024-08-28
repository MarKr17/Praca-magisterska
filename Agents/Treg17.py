from Agents.Cell import Cell
import random


class Treg17(Cell):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.proliferation_rate = self.model.Proliferation_rate["T-cell"]
        self.health = self.model.Health["T-cell"]
        self.dmg_factor = self.model.Dmg_factor["T-cell"]
        self.reactive_to = ["EBNA1"]
        self.activated = False
        self.antigen_presented = ''
        self.activated_proliferation_rate = int(self.proliferation_rate)*2

    def step(self):
        self.move()
        self.activation()
        self.cytokine_release()
        self.proliferation()
        self.calculate_dmg()
        if self.health <= 0:
            self.death()

    def proliferation(self):
        r = random.randint(0, 99)
        if r < self.proliferation_rate:
            n = Treg17(self.model.ID, self.model)
            self.model.ID += 1
            n.pos = self.child_pos()
            n.calculate_side()
            n.reactive_to = self.reactive_to
            self.model.new_agents.append(n)
            self.tiredness += 1

    def activation(self):
        if self.antigen_presented in self.reactive_to:
            self.activated = True
            self.proliferation_rate = self.activated_proliferation_rate
        elif (self.model.hypothesis == "Bystander activation" and "MBP" in
              self.reactive_to):
            if self.model.cytokin_matrix[self.pos] >= self.cytokine_threshold:
                self.activated = True
                self.proliferation_rate = self.activated_proliferation_rate
        elif (self.model.hypothesis == "Epitope spreading" and
              self.antigen_presented == 'MBP'):
            r = random.randint(0, 99)
            if r < self.MBP_exposure:
                self.activated = True
                self.proliferation_rate = self.activated_proliferation_rate

    def cytokine_release(self):
        self.model.IL_17_matrix[self.pos[0],
                                self.pos[1]] += self.model.cytokine_amount
        self.model.IL_22_matrix[self.pos[0],
                                self.pos[1]] += self.model.cytokine_amount
        self.tiredness += 1
