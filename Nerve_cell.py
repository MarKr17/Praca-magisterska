import mesa


class Neuron(mesa.Agent):

    def __init__(self, unique_id, model, reg_rate):
        super().__init__(unique_id, model, reg_rate)
        self.reg_rate = reg_rate

    def step(self):
        if self.health <= 0:
            self.death()

    def death(self):
        self.model.kill_agents.append(self)

    def myelin_regeneration(self):
        cells = self.model.grid.iter_neighborhood(self.pos, radius=1,
                                                  moore=True)
        for (cell_contents, x, y) in cells:
            if len(cell_contents) == 0:
                n = Myelin(self.model.ID, self.model, self.unique_id)
                self.model.ID += 1
                self.model.new_agents.append(n)


class Myelin(mesa.Agent):

    def __init__(self, unique_id, model, neuron_id):
        super().__init__(unique_id, model, neuron_id)
        self.neuron_id = neuron_id

    def death(self):
        self.model.kill_agents.append(self)
