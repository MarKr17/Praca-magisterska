import math
import random
import numpy as np


def compute_gini(self):
    agent_healths = [agent.health for agent in self.schedule.agents]
    x = sorted(agent_healths)
    N = self.num_agents
    B = sum(xi * (N - i) for i, xi in enumerate(x)) / (N * sum(x))
    return 1 + (1 / N) - 2 * B


def update_cytokin_matrix(self):
    self.cytokin_matrix = (self.IFN_matrix + self.TGF_matrix +
                           self.IL_2_matrix + self.IL_4_matrix +
                           self.IL_6_matrix + self.IL_17_matrix +
                           self.IL_21_matrix + self.IL_22_matrix)


def cytokin_diffusion(self):
    self.IFN_matrix = diffusion(self.IFN_matrix)
    self.TGF_matrix = diffusion(self.TGF_matrix)
    self.IL_2_matrix = diffusion(self.IL_2_matrix)
    self.IL_4_matrix = diffusion(self.IL_4_matrix)
    self.IL_6_matrix = diffusion(self.IL_6_matrix)
    self.IL_17_matrix = diffusion(self.IL_17_matrix)
    self.IL_21_matrix = diffusion(self.IL_21_matrix)
    self.IL_22_matrix = diffusion(self.IL_22_matrix)
    self.MBP_matrix = diffusion(self.MBP_matrix)
    self.EBNA1_matrix = diffusion(self.EBNA1_matrix)
    self.MBP_matrix_antibody = diffusion(self.MBP_matrix)
    self.EBNA1_matrix_antibody = diffusion(self.EBNA1_matrix)


def diffusion(matrix):
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


def dissolve_cytokine(self):
    r = random.randint(0, 100)
    if r < self.cytokine_dis_rate:

        self.IFN_matrix = self.IFN_matrix-1
        self.IFN_matrix = np.clip(self.IFN_matrix, 0, None)

        self.TGF_matrix = self.TGF_matrix-1
        self.TGF_matrix = np.clip(self.TGF_matrix, 0, None)

        self.IL_2_matrix = self.IL_2_matrix-1
        self.IL_2_matrix = np.clip(self.IL_2_matrix, 0, None)

        self.IL_4_matrix = self.IL_4_matrix-1
        self.IL_4_matrix = np.clip(self.IL_4_matrix, 0, None)

        self.IL_6_matrix = self.IL_6_matrix-1
        self.IL_6_matrix = np.clip(self.IL_6_matrix, 0, None)

        self.IL_17_matrix = self.IL_17_matrix-1
        self.IL_17_matrix = np.clip(self.IL_17_matrix, 0, None)

        self.IL_21_matrix = self.IL_21_matrix-1
        self.IL_21_matrix = np.clip(self.IL_21_matrix, 0, None)

        self.IL_22_matrix = self.IL_22_matrix-1
        self.IL_22_matrix = np.clip(self.IL_22_matrix, 0, None)

        self.MBP_matrix = self.MBP_matrix-1
        self.MPB_matrix = np.clip(self.MBP_matrix, 0, None)

        self.EBNA1_matrix = self.EBNA1_matrix-1
        self.EBNA1_matrix = np.clip(self.EBNA1_matrix, 0, None)

        self.MBP_antibody_matrix = self.MBP_antibody_matrix-1
        self.MPB_antibody_matrix = np.clip(self.MBP_antibody_matrix, 0, None)

        self.EBNA1_antibody_matrix = self.EBNA1_antibody_matrix-1
        self.EBNA1_antibody_matrix = np.clip(self.EBNA1_antibody_matrix,
                                             0, None)


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


def barrier_cytokin_effect(self):
    for i in [6, 24]:
        for j in range(6, 25):
            self.barrier[i][j] += self.IFN_matrix[i][j]/100
            self.barrier[i][j] -= self.IL_22_matrix[i][j]/100
            self.barrier[i][j] -= self.IL_17_matrix[i][j]/100
