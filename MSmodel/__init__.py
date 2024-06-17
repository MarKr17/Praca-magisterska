import mesa
import numpy as np


class MSModel(mesa.Model):
    from ._creating_agents import (createNeurons, createB_cells,
                                   createT_naive_cells, createViruses,
                                   create_APCs)
    from ._step import (step, killing_agents, adding_agents, start_infection)
    from ._grid_functions import (cytokin_diffusion, dissolve_cytokine,
                                  possible_positions, update_cytokin_matrix,
                                  barrier_cytokin_effect)

    def __init__(self):
        from ._computing import (compute_B_cells, compute_Myelin,
                                 compute_Neurons, compute_T_naive_cells,
                                 compute_Virus)
        self.num_t = 20  # number of T-cells
        self.num_b = 20  # number of B-cells
        self.num_APC = 10  # number of APCs
        self.size = 30
        self.neuron_number = 9
        self.neuron_positions = [[12, 12], [15, 12], [18, 12],
                                 [12, 15], [15, 15], [18, 15],
                                 [12, 18], [15, 18], [18, 18]]
        self.areas = np.zeros((self.size, self.size), dtype=int)
        for i in range(6, 25):
            self.areas[i][6] = 1
            self.areas[i][24] = 1
            if i in [6, 24]:
                for j in range(6, 25):
                    self.areas[i][j] = 1
        for i in range(7, 24):
            for j in range(7, 24):
                self.areas[i][j] = 2

        self.barrier = np.zeros((self.size, self.size), dtype=float)
        for i in [6, 24]:
            for j in range(6, 25):
                self.barrier[i][j] = 100
        self.hypothesis = "Molecular mimicry"
        self.kill_agents = []  # list of agents that died
        self.new_agents = []  # list of new agents to add
        self.ID = 0  # id number that is available at the moment
        self.cytokin_matrix = np.zeros((self.size, self.size), dtype=int)
        self.IFN_matrix = np.zeros((self.size, self.size), dtype=int)
        self.TGF_matrix = np.zeros((self.size, self.size), dtype=int)
        self.IL_2_matrix = np.zeros((self.size, self.size), dtype=int)
        self.IL_4_matrix = np.zeros((self.size, self.size), dtype=int)
        self.IL_6_matrix = np.zeros((self.size, self.size), dtype=int)
        self.IL_17_matrix = np.zeros((self.size, self.size), dtype=int)
        self.IL_21_matrix = np.zeros((self.size, self.size), dtype=int)
        self.IL_22_matrix = np.zeros((self.size, self.size), dtype=int)
        self.MBP_matrix = np.zeros((self.size, self.size), dtype=int)
        self.EBNA1_matrix = np.zeros((self.size, self.size), dtype=int)
        self.MBP_antibody_matrix = np.zeros((self.size, self.size), dtype=int)
        self.EBNA1_antibody_matrix = np.zeros((self.size, self.size),
                                              dtype=int)
        self.cytokine_dis_rate = 5
        self.infection_chance = 5
        self.grid = mesa.space.MultiGrid(self.size, self.size, True)
        # Create scheduler and assign it to the model
        self.schedule = mesa.time.RandomActivation(self)
        self.datacollector = mesa.DataCollector(
            model_reporters={"T-cell population": compute_T_naive_cells,
                             "B-cell population": compute_B_cells,
                             "Neuron population": compute_Neurons,
                             "Myelin population": compute_Myelin,
                             "Virus population": compute_Virus}
        )
        self.createNeurons()
        self.createT_naive_cells()
        self.createB_cells()
        self.create_APCs()
