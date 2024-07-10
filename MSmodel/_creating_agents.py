from Agents.Neuron import Neuron
from Agents.B_cell import B_cell
from Agents.T_naive_cell import T_naive_cell
from Agents.Th_cell import Th_cell
from Agents.Virus import Virus
from Agents.APC import APC
import random


def createNeurons(self):
    for i in range(self.neuron_number):
        n = Neuron(self.ID, self, 10)
        # Add neuron to scheduler
        self.schedule.add(n)
        # Add neuron to assinged grid cell
        x = self.neuron_positions[i][0]
        y = self.neuron_positions[i][1]
        self.grid.place_agent(n, (x, y))
        self.ID += 1


def createT_naive_cells(self, number):
    positions = self.possible_positions()
    for i in range(number):
        a = T_naive_cell(self.ID, self)
        # Add the agent to the scheduler
        self.schedule.add(a)
        a.pos = random.choice(positions)
        self.grid.place_agent(a, a.pos)
        a.calculate_side()
        self.ID += 1


def createThcells(self, number):
    positions = self.possible_positions()
    for i in range(number):
        a = Th_cell(self.ID, self)
        # Add the agent to the scheduler
        self.schedule.add(a)
        a.pos = random.choice(positions)
        self.grid.place_agent(a, a.pos)
        a.calculate_side()
        self.ID += 1


def createB_cells(self, number):
    positions = self.possible_positions()
    for i in range(number):
        a = B_cell(self.ID, self)
        # Add the agent to the scheduler
        self.schedule.add(a)
        a.pos = random.choice(positions)
        self.grid.place_agent(a, a.pos)
        a.calculate_side()
        self.ID += 1


def createViruses(self, n):
    positions = self.possible_positions()
    for i in range(n):
        a = Virus(self.ID, self)
        # Add the agent to the scheduler
        self.schedule.add(a)
        a.pos = random.choice(positions)
        self.grid.place_agent(a, a.pos)
        a.calculate_side()
        self.ID += 1


def create_APCs(self, number):
    positions = self.possible_positions()
    for i in range(number):
        a = APC(self.ID, self)
        # Add the agent to the scheduler
        self.schedule.add(a)
        a.pos = random.choice(positions)
        self.grid.place_agent(a, a.pos)
        a.calculate_side()
        self.ID += 1
