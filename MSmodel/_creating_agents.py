from Neuron import Neuron
from T_cell import T_cell
from B_cell import B_cell
from Virus import Virus
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


def createT_cells(self):
    positions = self.possible_positions()
    for i in range(self.num_t):
        a = T_cell(self.ID, self, proliferation_rate=0,
                   cytokin_rate=50)
        # Add the agent to the scheduler
        self.schedule.add(a)
        pos = random.choice(positions)
        self.grid.place_agent(a, pos)
        self.ID += 1


def createB_cells(self):
    positions = self.possible_positions()
    for i in range(self.num_b):
        a = B_cell(self.ID, self, proliferation_rate=0)
        # Add the agent to the scheduler
        self.schedule.add(a)
        pos = random.choice(positions)
        self.grid.place_agent(a, pos)
        self.ID += 1


def createViruses(self, n):
    positions = self.possible_positions()
    for i in range(n):
        a = Virus(self.ID, self)
        # Add the agent to the scheduler
        self.schedule.add(a)
        pos = random.choice(positions)
        self.grid.place_agent(a, pos)
        self.ID += 1
