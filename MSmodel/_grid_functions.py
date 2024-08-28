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


def cytokin_diffusion(self, radius):
    self.IFN_matrix = self.diffusion(self.IFN_matrix, radius)
    self.TGF_matrix = self.diffusion(self.TGF_matrix, radius)
    self.IL_2_matrix = self.diffusion(self.IL_2_matrix, radius)
    self.IL_4_matrix = self.diffusion(self.IL_4_matrix, radius)
    self.IL_6_matrix = self.diffusion(self.IL_6_matrix, radius)
    self.IL_17_matrix = self.diffusion(self.IL_17_matrix, radius)
    self.IL_21_matrix = self.diffusion(self.IL_21_matrix, radius)
    self.IL_22_matrix = self.diffusion(self.IL_22_matrix, radius)
    self.MBP_matrix = self.diffusion(self.MBP_matrix, radius)
    self.EBNA1_matrix = self.diffusion(self.EBNA1_matrix, radius)
    self.MBP_antibody_matrix = self.diffusion(self.MBP_antibody_matrix, radius)
    self.EBNA1_antibody_matrix = self.diffusion(self.EBNA1_antibody_matrix,
                                                radius)


def diffusion(self, matrix, radius):
    for x in range(radius, len(matrix)-radius):
        for y in range(radius, len(matrix)-radius):
            # averege amount of cytokine in neighbor cells
            if matrix[x][y] >= 4:
                min = matrix[x][y]
                sum = min
                pos = (x, y)
                positions = []
                positions.append(pos)
                neighborhood = self.grid.get_neighborhood(pos, moore=True,
                                                          include_center=False,
                                                          radius=radius)
                for n in neighborhood:
                    if matrix[n] < min:
                        pos = n
                        positions = []
                        positions.append(pos)
                        sum = min
                        min = matrix[n]
                    elif matrix[n] == min:
                        positions.append(pos)
                        sum += matrix[n]
                # r = math.floor((matrix[x][y] - min)/2)
                r = int((matrix[x][y] - min)/len(positions))
                matrix[x][y] -= r
                for pos in positions:
                    matrix[pos] += r
    return matrix


def dissolve_cytokine(self):
    r = random.randint(0, 100)
    if r < self.cytokine_dis_rate:

        self.IFN_matrix -= 1
        self.IFN_matrix = np.clip(self.IFN_matrix, 0, 100)

        self.TGF_matrix -= 1
        self.TGF_matrix = np.clip(self.TGF_matrix, 0, 100)

        self.IL_2_matrix -= 1
        self.IL_2_matrix = np.clip(self.IL_2_matrix, 0, 100)

        self.IL_4_matrix -= 1
        self.IL_4_matrix = np.clip(self.IL_4_matrix, 0, 100)

        self.IL_6_matrix -= 1
        self.IL_6_matrix = np.clip(self.IL_6_matrix, 0, 100)

        self.IL_17_matrix -= 1
        self.IL_17_matrix = np.clip(self.IL_17_matrix, 0, 100)

        self.IL_21_matrix -= 1
        self.IL_21_matrix = np.clip(self.IL_21_matrix, 0, 100)

        self.IL_22_matrix -= 1
        self.IL_22_matrix = np.clip(self.IL_22_matrix, 0, 100)

        self.MBP_matrix -= 1
        self.MBP_matrix = np.clip(self.MBP_matrix, 0, 100)

        self.EBNA1_matrix -= 1
        self.EBNA1_matrix = np.clip(self.EBNA1_matrix, 0, 100)

        self.MBP_antibody_matrix -= 1
        self.MBP_antibody_matrix = np.clip(self.MBP_antibody_matrix, 0, 100)

        self.EBNA1_antibody_matrix -= 1
        self.EBNA1_antibody_matrix = np.clip(self.EBNA1_antibody_matrix,
                                             0, 100)


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
    for i in range(6, 25):
        self.calculate_cytokine_effect(i, 6)
        self.calculate_cytokine_effect(i, 24)
        if i in [6, 24]:
            for j in range(6, 25):
                self.calculate_cytokine_effect(i, j)


def calculate_cytokine_effect(self, i, j):
    if self.barrier[i][j] < 100:
        self.barrier[i][j] += int(self.IFN_matrix[i][j]*2)
    self.barrier[i][j] -= int(self.IL_22_matrix[i][j]/3)
    self.barrier[i][j] -= int(self.IL_17_matrix[i][j]/3)
