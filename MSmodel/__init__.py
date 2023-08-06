import mesa
import numpy as np


class MSModel(mesa.Model):
    from ._creating_agents import (createNeurons, createB_cells,
                                   createT_cells)
    from ._step import (step, killing_agents, adding_agents)
    from ._grid_functions import (cytokine_diffusion, dissolve_cytokine)

    def __init__(self, width, height):
        self.num_t = 20  # number of T-cells
        self.num_b = 20  # number of B-cells
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
        """
        self.datacollector = mesa.DataCollector(
            model_reporters={"Gini": compute_gini},
            agent_reporters={"Health": "health"}
        )"""
        self.createNeurons()
        self.createT_cells()
        self.createB_cells()
