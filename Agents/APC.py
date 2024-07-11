from Agents.Cell import Cell
from Agents.B_cell import B_cell
from Agents.Plasma_cell import Plasma_cell
from Agents.Neuron import Neuron
from Agents.T_naive_cell import T_naive_cell
from Agents.Th_cell import Th_cell
from Agents.Virus import Virus
import random


class APC(Cell):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.MHC_grow_rate = 5
        self.num_MHC = 0
        self.antigen_attached = ''
        self.phagocytosis_rate = 50
        self.antibodies_threshold = 5
        self.proliferation_rate = self.model.Proliferation_rate["APC"]
        self.health = self.model.Health["APC"]
        self.dmg_factor = self.model.Dmg_factor["APC"]

    def step(self):
        self.move()
        r = random.randint(0, 99)
        if r < self.proliferation_rate:
            self.proliferation()
        elif r < self.phagocytosis_rate:
            self.phagocytosis()
        else:
            self.antigen_presentation()
        if self.antigen_attached == '':
            self.antigen_attachment()

        self.cytokine_release()
        self.calculate_dmg()
        if self.health <= 0:
            self.death()

    def proliferation(self):
        n = APC(self.model.ID, self.model)
        n.pos = self.child_pos()
        n.calculate_side()
        self.model.ID += 1
        self.model.new_agents.append(n)
        self.tiredness += 1

    def antigen_attachment(self):
        MBP = self.model.MBP_matrix[self.pos[0], self.pos[1]]
        EBNA1 = self.model.EBNA1_matrix[self.pos[0], self.pos[1]]
        if MBP + EBNA1 != 0:
            if MBP > EBNA1:
                self.antigen_attached = "MBP"
                self.model.MBP_matrix[self.pos[0], self.pos[1]] -= 1
            else:
                self.antigen_attached = "EBNA1"
                self.model.EBNA1_matrix[self.pos[0], self.pos[1]] -= 1

    def antigen_presentation(self):
        neighbors = self.model.grid.get_neighbors(self.pos, moore=True)
        neighbors_copy = neighbors.copy()
        for n in neighbors_copy:
            if not isinstance(n, (B_cell, Plasma_cell, Th_cell, T_naive_cell)):
                neighbors.remove(n)
        if len(neighbors) > 0:
            agent = random.choice(neighbors)
            agent.antigen_presented = self.antigen_attached
            self.antigen_attached = ''
            self.tiredness += 1
            name = type(agent).__name__
            name = str(name)
            if name in ['T_naive_cell', 'Th_cell']:
                self.epitope_spreading(agent)

    def phagocytosis(self):
        neighbors = self.model.grid.get_neighbors(self.pos, moore=True)
        neighbors_copy = neighbors.copy()
        for n in neighbors_copy:
            if not isinstance(n, (Neuron, Virus)):
                neighbors.remove(n)
            elif n.attached_antibodies < self.antibodies_threshold:
                neighbors.remove(n)
        if len(neighbors) > 0:
            b = random.choice(neighbors)
            if isinstance(b, Neuron):
                dmg = int(b.myelin_health * 0.1)
                b.current_myelin_health -= dmg
                b.attached_antibodies = 0
            else:
                b.death()
            self.tiredness += 1

    def cytokine_release(self):
        if self.antigen_attached == "EBNA1":
            self.model.IL_6_matrix[self.pos[0],
                                   self.pos[1]] += self.model.cytokine_amount
            self.model.IL_21_matrix[self.pos[0],
                                    self.pos[1]] += self.model.cytokine_amount
            self.model.TGF_matrix[self.pos[0],
                                  self.pos[1]] += self.model.cytokine_amount
            self.tiredness += 1

    def epitope_spreading(self, agent):
        if agent.antigen_presented == 'MBP':
            agent.MBP_exposure += 1
