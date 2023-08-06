from Neuron import Neuron
from T_cell import T_cell
from B_cell import B_cell


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
    for i in range(self.num_t):
        a = T_cell(self.ID, self, proliferation_rate=0,
                   cytokin_rate=50)
        # Add the agent to the scheduler
        self.schedule.add(a)
        # Add the agent to a random grid cell
        x = self.random.randrange(self.grid.width)
        y = self.random.randrange(self.grid.height)
        self.grid.place_agent(a, (x, y))
        self.ID += 1


def createB_cells(self):
    for i in range(self.num_b):
        a = B_cell(self.ID, self, proliferation_rate=0)
        # Add the agent to the scheduler
        self.schedule.add(a)
        # Add the agent to a random grid cell
        x = self.random.randrange(self.grid.width)
        y = self.random.randrange(self.grid.height)
        self.grid.place_agent(a, (x, y))
        self.ID += 1
