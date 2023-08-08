def compute_T_naive_cells(self):
    from Agents.T_naive_cell import T_naive_cell
    T = 0
    for agent in self.schedule.agents:
        if type(agent) is T_naive_cell:
            T += 1
    return T


def compute_B_cells(self):
    from Agents.B_cell import B_cell
    B = 0
    for agent in self.schedule.agents:
        if type(agent) is B_cell:
            B += 1
    return B


def compute_Neurons(self):
    from Agents.Neuron import Neuron
    N = 0
    for agent in self.schedule.agents:
        if type(agent) is Neuron:
            N += 1
    return N


def compute_Myelin(self):
    from Agents.Neuron import Neuron
    M = 0
    for agent in self.schedule.agents:
        if type(agent) is Neuron:
            M += agent.myelin_health
    return M


def compute_Virus(self):
    from Agents.Virus import Virus
    V = 0
    for agent in self.schedule.agents:
        if type(agent) is Virus:
            V += 1
    return V
