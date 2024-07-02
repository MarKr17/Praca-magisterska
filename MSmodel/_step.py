def step(self):
    """Advance the model by one step."""
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
