from Agents.T_naive_cell import T_naive_cell
from Agents.Th_cell import Th_cell
from Agents.B_cell import B_cell
from Agents.APC import APC
from Agents.Neuron import Neuron
from Agents.Virus import Virus
from Agents.Plasma_cell import Plasma_cell
from Agents.Th0 import Th0
from Agents.Th1 import Th1
from Agents.Th2 import Th2
from Agents.Tpato17 import Tpato17
from Agents.Treg17 import Treg17


def compute_T_naive_cells(self):
    T = 0
    for agent in self.schedule.agents:
        if type(agent) is T_naive_cell:
            T += 1
    return T


def compute_Th_cells(self):
    T = 0
    for agent in self.schedule.agents:
        if type(agent) is Th_cell:
            T += 1
    return T


def compute_B_cells(self):
    B = 0
    for agent in self.schedule.agents:
        if type(agent) is B_cell:
            B += 1
    return B


def compute_APC_cells(self):
    apc = 0
    for agent in self.schedule.agents:
        if type(agent) is APC:
            apc += 1
    return apc


def compute_Neurons(self):
    N = 0
    for agent in self.schedule.agents:
        if type(agent) is Neuron:
            N += 1
    return N


def compute_Myelin(self):
    M = 0
    for agent in self.schedule.agents:
        if type(agent) is Neuron:
            M += agent.current_myelin_health
    return M


def compute_Virus(self):
    V = 0
    for agent in self.schedule.agents:
        if type(agent) is Virus:
            V += 1
    return V


def computePlasma_cells(self):
    P = 0
    for agent in self.schedule.agents:
        if type(agent) is Plasma_cell:
            P += 1
    return P


def compute_Th0_cells(self):
    T = 0
    for agent in self.schedule.agents:
        if type(agent) is Th0:
            T += 1
    return T


def compute_Th1_cells(self):
    T = 0
    for agent in self.schedule.agents:
        if type(agent) is Th1:
            T += 1
    return T


def compute_Th2_cells(self):
    T = 0
    for agent in self.schedule.agents:
        if type(agent) is Th2:
            T += 1
    return T


def compute_Tpato17_cells(self):
    T = 0
    for agent in self.schedule.agents:
        if type(agent) is Tpato17:
            T += 1
    return T


def compute_Treg17_cells(self):
    T = 0
    for agent in self.schedule.agents:
        if type(agent) is Treg17:
            T += 1
    return T
