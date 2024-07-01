import random
from Agents.Agent import Agent


class Cell(Agent):

    def __init__(self, unique_id, model):
        # Pass the parameters to the parent class.
        super().__init__(unique_id, model)

        # Create the agent's attribute and set the initial values.
        self.health = 50
        self.tiredness = 0
        self.proliferation_rate = 0
        self.penetration_chance = 25
        self.dmg_factor = 1

    def step(self):
        self.move()

    def death(self):
        self.model.kill_agents.append(self)

    def calculate_dmg(self):
        dmg = int(self.tiredness/self.dmg_factor)
        self.health -= dmg
        if self.health < 0:
            self.health = 0

    def move(self):
        positions = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=False)
        positions_copy = positions.copy()
        for pos in positions_copy:
            if self.area != 2:
                if self.model.areas[pos[0]][pos[1]] == 2:
                    positions.remove(pos)
        new_position = self.random.choice(positions)
        x = new_position[0]
        y = new_position[1]
        if self.model.areas[x][y] == 1:
            chance = self.penetration_chance + 100 - self.model.barrier[x][y]
            chance = int(chance/100)
            r = random.randint(0, 100)
            if r < chance:
                for i in [-2, -1, 1, 2]:
                    for j in [-2, -1, 1, 2]:
                        if self.model.areas[x+i][y+j] == self.o_side:
                            new_position = (x+i, y+j)
                            if self.o_side == 1:
                                self.o_side = 2
                            else:
                                self.o_side = 1
                            break
            else:
                new_position = self.pos
        self.area = self.model.areas[new_position[0]][new_position[1]]
        self.model.grid.move_agent(self, new_position)
