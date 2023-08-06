import mesa
import numpy as np
import random
import math
from T_cell import T_cell
from Neuron import Neuron


def compute_gini(model):
    agent_healths = [agent.health for agent in model.schedule.agents]
    x = sorted(agent_healths)
    N = model.num_agents
    B = sum(xi * (N - i) for i, xi in enumerate(x)) / (N * sum(x))
    return 1 + (1 / N) - 2 * B


def cytokine_diffusion(matrix):
    for x in range(1, len(matrix)-1):
        for y in range(1, len(matrix)-1):
            # averege amount of cytokine in neighbor cells
            if matrix[x][y] > 4:
                min = matrix[x][y]
                pos = (0, 0)
                for i in range(x-1, x+1):
                    for j in range(y-1, y+1):
                        if i == x and j == y:
                            continue
                        elif matrix[i][j] < min:
                            pos = (i, j)
                            min = matrix[i][j]
                r = math.floor((matrix[x][y] - min)/2)
                matrix[x][y] -= r
                matrix[pos[0]][pos[1]] += r
    return matrix


class MSModel(mesa.Model):
    """A model with some number of agents."""
    def __init__(self, N, width, height):
        self.num_agents = N
        self.width = width
        self.neuron_number = 9
        self.neuron_positions = [[12, 12], [15, 12], [18, 12],
                                 [12, 15], [15, 15], [18, 15],
                                 [12, 18], [15, 18], [18, 18]]
        self.areas = np.zeros((width, width), dtype=int)
        for i in range(6, 25):
            self.areas[i][6] = 1
            self.areas[i][24] = 1
            if i in [6, 24]:
                for j in range(6, 25):
                    self.areas[i][j] = 1
        for i in range(7, 24):
            for j in range(7, 24):
                self.areas[i][j] = 2

        self.kill_agents = []  # list of agents that died
        self.new_agents = []  # list of new agents to add
        self.ID = 0  # id number that is available at the moment
        self.cytokine_matrix = np.zeros((width, width), dtype=int)
        self.cytokine_dis_rate = 5
        self.grid = mesa.space.MultiGrid(width, height, True)
        # Create scheduler and assign it to the model
        self.schedule = mesa.time.RandomActivation(self)
        self.datacollector = mesa.DataCollector(
            model_reporters={"Gini": compute_gini},
            agent_reporters={"Health": "health"}
        )
        # Create neurons
        for i in range(self.neuron_number):
            n = Neuron(self.ID, self, 10)
            # Add neuron to scheduler
            self.schedule.add(n)
            # Add neuron to assinged grid cell
            x = self.neuron_positions[i][0]
            y = self.neuron_positions[i][1]
            self.grid.place_agent(n, (x, y))
            self.ID += 1
        print(self.ID)
        # Create agents
        for i in range(self.num_agents):
            a = T_cell(self.ID, self, proliferation_rate=0,
                       cytokin_rate=50)
            # Add the agent to the scheduler
            self.schedule.add(a)
            # Add the agent to a random grid cell
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))
            self.ID += 1

    def step(self):
        """Advance the model by one step."""
        self.datacollector.collect(self)
        self.kill_agents = []
        self.schedule.step()
        with open("agents.txt", 'w') as f:
            for key, value in self.schedule._agents.items():
                f.write('%s:%s\n' % (key, value))
        for x in self.kill_agents:
            self.schedule.remove(x)
            self.grid.remove_agent(x)
            self.kill_agents.remove(x)
        for n in self.new_agents:
            self.schedule.add(n)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(n, (x, y))
            self.new_agents.remove(n)
        # disolving cytokine
        r = random.randint(0, 100)
        if r < self.cytokine_dis_rate:
            self.cytokine_matrix = self.cytokine_matrix-1
            self.cytokine_matrix = np.clip(self.cytokine_matrix, 0, None)
        self.cytokine_matrix = cytokine_diffusion(self.cytokine_matrix)
