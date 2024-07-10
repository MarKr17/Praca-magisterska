def step(self):
    """Advance the model by one step."""
    if self.schedule.steps == 0:
        self.hypothesis_switch()
    elif self.schedule.steps % 100 == 0:
        self.createT_naive_cells(int(self.Cell_numbers["T-cell"]/2))
        self.createThcells(int(self.Cell_numbers["Th-cell"]/2))
        self.createB_cells(int(self.Cell_numbers["B-cell"]/2))
        self.create_APCs(int(self.Cell_numbers["APC"]/2))
    self.kill_agents = []
    self.new_agents = []
    self.schedule.step()
    with open("agents.txt", 'w') as f:
        for key, value in self.schedule._agents.items():
            f.write('%s:%s\n' % (key, value))
    self.killing_agents()
    self.adding_agents()
    self.dissolve_cytokine()
    self.cytokin_diffusion()
    self.update_cytokin_matrix()
    self.barrier_cytokin_effect()
    self.start_infection()
    self.datacollector.collect(self)


def killing_agents(self):
    for x in self.kill_agents:
        self.schedule.remove(x)
        self.grid.remove_agent(x)


def adding_agents(self):
    for n in self.new_agents:
        self.schedule.add(n)
        self.grid.place_agent(n, n.pos)


def start_infection(self):
    if self.schedule.steps == 5:
        self.createViruses(50)


def hypothesis_switch(self):
    if self.hypothesis == "Molecullar mimicry":
        self.molecullar_mimicry()
    elif self.hypothesis == "Bystander activation":
        self.bystander_activation()
    elif self.hypothesis == "Epitope spreading":
        self.epitope_spreading()


def molecullar_mimicry(self):
    for agent in self.schedule.agents:
        name = type(agent).__name__
        name = str(name)
        if name[0] == 'T':
            agent.reactive_to = ["EBNA1", "MBP"]


def bystander_activation(self):
    # number of auto-reactive t-cells
    nt = int(self.Cell_numbers["T-cell"]*0.2)
    # number of auto-reactive th-cells
    nth = int(self.Cell_numbers["Th-cell"]*0.2)
    for agent in self.schedule.agents:
        name = type(agent).__name__
        name = str(name)
        if name == 'T_naive cell' and nt > 0:
            agent.reactive_to = "MBP"
            nt -= 1
        elif name == 'Th_cell' and nth > 0:
            agent.reactive_to = "MBP"
            nth -= 1


def epitope_spreading(self):
    myelin_dmg = 5
    for agent in self.schedule.agents:
        name = type(agent).__name__
        name = str(name)
        if name == 'Neuron':
            agent.myelin_health -= myelin_dmg
            agent.MBP_release(myelin_dmg)
