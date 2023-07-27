import mesa


class Lymphocyte(mesa.Agent):

    def __init__(self, unique_id, model):
        # Pass the parameters to the parent class.
        super().__init__(unique_id, model)

        # Create the agent's attribute and set the initial values.
        self.health = 1

    def step(self):
        self.move()

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=False)
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    def proliferation(self):
        n = Lymphocyte(self.model.ID, self.model)
        self.model.ID += 1
        self.model.new_agents.append(n)

    def death(self):
        self.model.kill_agents.append(self)
