import math
import random
import numpy as np


def compute_gini(self):
    agent_healths = [agent.health for agent in self.schedule.agents]
    x = sorted(agent_healths)
    N = self.num_agents
    B = sum(xi * (N - i) for i, xi in enumerate(x)) / (N * sum(x))
    return 1 + (1 / N) - 2 * B


def cytokine_diffusion(self):
    matrix = self.cytokine_matrix
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
    self.cytokine_matrix = matrix


def dissolve_cytokine(self):
    r = random.randint(0, 100)
    if r < self.cytokine_dis_rate:
        self.cytokine_matrix = self.cytokine_matrix-1
        self.cytokine_matrix = np.clip(self.cytokine_matrix, 0, None)


def possible_positions(self):
    positions = []
    for x in range(self.size):
        for y in range(self.size):
            positions.append((x, y))
    positions_copy = positions.copy()
    for pos in positions_copy:
        a = self.areas[pos[0]][pos[1]]
        if a in [1, 2]:
            positions.remove(pos)
    return positions
