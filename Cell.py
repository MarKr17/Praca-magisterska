import mesa
import random


class Cell(mesa.Agent):

    def __init__(self, unique_id, model, proliferation_rate):
        # Pass the parameters to the parent class.
        super().__init__(unique_id, model)

        # Create the agent's attribute and set the initial values.
        self.health = 20
        self.tiredness = 0
        self.proliferation_rate = proliferation_rate
        self.penetration_chance = 25

    def step(self):
        self.move()

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=False)
        if self.model.areas[self.pos[0]][self.pos[1]] == 2:
            for pos in possible_steps:
                if self.model.areas[pos[0]][pos[1]] != 2:
                    possible_steps.remove(pos)
        new_position = self.random.choice(possible_steps)
        x = new_position[0]
        y = new_position[1]
        if self.model.areas[x][y] == 1:
            r = random.randint(0, 100)
            if r < self.penetration_chance:
                for i in [-2, -1, 1, 2]:
                    for j in [-2, -1, 1, 2]:
                        if self.model.areas[x+i][y+j] == 2:
                            new_position = (x+i, y+j)
                            break
            else:
                new_position = self.pos

        self.model.grid.move_agent(self, new_position)

    def proliferation(self):
        r = random.randint(0, 100)
        if r < self.proliferation_rate:
            n = Cell(self.model.ID, self.model, proliferation_rate=0)
            self.model.ID += 1
            self.model.new_agents.append(n)
            self.tiredness += 1

    def death(self):
        self.model.kill_agents.append(self)
