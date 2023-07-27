import mesa
from Lymphocyte import Lymphocyte


def compute_gini(model):
    agent_healths = [agent.health for agent in model.schedule.agents]
    x = sorted(agent_healths)
    N = model.num_agents
    B = sum(xi * (N - i) for i, xi in enumerate(x)) / (N * sum(x))
    return 1 + (1 / N) - 2 * B


class MSModel(mesa.Model):
    """A model with some number of agents."""
    def __init__(self, N, width, height):
        self.num_agents = N
        self.width = width
        self.kill_agents = []  # list of agents that died
        self.new_agents = []  # list of new agents to add
        self.ID = 0  # id number that is available at the moment
        self.grid = mesa.space.MultiGrid(width, height, True)
        # Create scheduler and assign it to the model
        self.schedule = mesa.time.RandomActivation(self)
        self.datacollector = mesa.DataCollector(
            model_reporters={"Gini": compute_gini},
            agent_reporters={"Health": "health"}
        )
        # Create agents
        for i in range(self.num_agents):
            a = Lymphocyte(self.ID, self)
            # Add the agent to the scheduler
            self.schedule.add(a)
            # Add the agent to a random grid cell
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))
            self.ID += 1

    def step(self):
        """Advance the model by one step."""
        self.datacollector.collect(self)
        self.schedule.step()
        for x in self.kill_agents:
            self.schedule.remove(x)
            self.grid.remove_agent(x)
            self.kill_agents.remove(x)
        for n in self.new_agents:
            self.schedule.add(n)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(n, (x, y))
