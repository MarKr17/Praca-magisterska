import mesa
import numpy as np


class MSModel(mesa.Model):
    from ._creating_agents import (createNeurons, createB_cells,
                                   createT_naive_cells, createViruses,
                                   create_APCs, createThcells)
    from ._step import (step, killing_agents, adding_agents, start_infection)
    from ._grid_functions import (cytokin_diffusion, dissolve_cytokine,
                                  possible_positions, update_cytokin_matrix,
                                  barrier_cytokin_effect)

    def __init__(self):
        from ._computing import (compute_B_cells, compute_Myelin,
                                 compute_Neurons, compute_T_naive_cells,
                                 compute_Virus, computePlasma_cells,
                                 compute_Th_cells, compute_Th0_cells,
                                 compute_Th1_cells, compute_Th2_cells,
                                 compute_Tpato17_cells, compute_Treg17_cells,
                                 compute_APC_cells, compute_cytokine_levels,
                                 compute_IFN_levels, compute_TGF_levels,
                                 compute_IL_2_levels, compute_IL_4_levels,
                                 compute_IL_6_levels, compute_IL_17_levels,
                                 compute_IL_21_levels, compute_IL_22_levels,
                                 compute_MBP_levels, compute_EBNA1_levels,
                                 compute_MBP_antibody_levels,
                                 compute_EBNA1_antibody_levels,
                                 computeB_cells_presented,
                                 compute_APC_antigen_attached,
                                 computeB_cells_activated,
                                 computeB_cells_latent,
                                 computeB_cells_lytic)
        self.num_t = 20  # number of T-cells
        self.num_th = 20  # number of Th-cells
        self.num_b = 20  # number of B-cells
        self.num_APC = 20  # number of APCs
        self.APC_health = 20
        self.proliferation_rate = 20
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
        self.cytokine_dis_rate = 10
        self.infection_chance = 5
        self.grid = mesa.space.MultiGrid(self.size, self.size, True)
        # Create scheduler and assign it to the model
        self.schedule = mesa.time.RandomActivation(self)
        self.datacollector = mesa.DataCollector(
            model_reporters={"T-cell population": compute_T_naive_cells,
                             "Th-cell population": compute_Th_cells,
                             "B-cell population": compute_B_cells,
                             "APC population": compute_APC_cells,
                             "Neuron population": compute_Neurons,
                             "Myelin population": compute_Myelin,
                             "Virus population": compute_Virus,
                             "Plasma cell population": computePlasma_cells,
                             "Th0 population": compute_Th0_cells,
                             "Th1 population": compute_Th1_cells,
                             "Th2 population": compute_Th2_cells,
                             "Tpato17 population": compute_Tpato17_cells,
                             "Treg17 population": compute_Treg17_cells,
                             "Cytokine levels": compute_cytokine_levels,
                             "IFN levels": compute_IFN_levels,
                             "TGF levels": compute_TGF_levels,
                             "IL-2 levels": compute_IL_2_levels,
                             "IL-4 levels": compute_IL_4_levels,
                             "IL-6 levels": compute_IL_6_levels,
                             "IL-17 levels": compute_IL_17_levels,
                             "IL-21 levels": compute_IL_21_levels,
                             "IL-22 levels": compute_IL_22_levels,
                             "MBP levels": compute_MBP_levels,
                             "EBNA1 levels": compute_EBNA1_levels,
                             "MBP antibody levels":
                                 compute_MBP_antibody_levels,
                             "EBNA1 antibody levels":
                                 compute_EBNA1_antibody_levels,
                             "B cells antigen presented":
                                 computeB_cells_presented,
                             "APC antigen attached":
                                 compute_APC_antigen_attached,
                             "B cells activated": computeB_cells_activated,
                             "B cells latent": computeB_cells_latent,
                             "B cells lytic": computeB_cells_lytic}
        )
        self.createNeurons()
        self.createT_naive_cells()
        self.createThcells()
        self.createB_cells()
        self.create_APCs()
