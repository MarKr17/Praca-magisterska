from Agents.Cell import Cell


class B_cell(Cell):
    def __init__(self, unique_id, model, proliferation_rate):
        super().__init__(unique_id, model, proliferation_rate)
        self.infected = False
        self.latency = ""
        self.proteins = []

    def step(self):
        self.move()
        self.proliferation()
        if self.infected is True and self.latency == "latency I":
            self.viral_replication()
            self.health = 0
        if self.health <= 0:
            self.death()

    def viral_replication(self):
        from Agents.Virus import Virus
        neighborhood = self.model.grid.neighborhood(self.pos, moore=True,
                                                    include_center=False)
        neighborhood_copy = neighborhood.copy()
        for n in neighborhood_copy:
            a = self.model.areas[n[0]][n[1]]
            if a == 1:
                neighborhood.remove(n)
        for n in neighborhood:
            v = Virus(self.model.ID, self.model)
            self.model.ID += 1
            self.model.new_agents.append(v)
            self.tiredness += 1

    def protein_production(self):
        if self.latency == "latency I":
            self.proteins.append("EBNA1")
