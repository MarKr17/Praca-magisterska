import mesa
import random


class Lymphocyte(mesa.Agent):

    def __init__(self, unique_id, model, proliferation_rate):
        # Pass the parameters to the parent class.
        super().__init__(unique_id, model)

        # Create the agent's attribute and set the initial values.
        self.health = 20
        self.tiredness = 0
        self.proliferation_rate = proliferation_rate

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
        r = random.randint(0, 100)
        if r < self.proliferation_rate:
            n = Lymphocyte(self.model.ID, self.model, proliferation_rate=0)
            self.model.ID += 1
            self.model.new_agents.append(n)
            self.tiredness += 1

    def death(self):
        self.model.kill_agents.append(self)
