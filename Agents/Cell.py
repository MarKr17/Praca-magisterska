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
        self.calculate_side()
        positions = self.possible_positions()
        if len(positions) > 0:
            new_position = self.random.choice(positions)
            x = new_position[0]
            y = new_position[1]
            if self.model.areas[x][y] == 1:
                chance = 100 - self.model.barrier[x][y]
                r = random.randint(0, 100)
                if r < chance:
                    for i in [-2, -1, 1, 2]:
                        for j in [-2, -1, 1, 2]:
                            if self.model.areas[x+i][y+j] == self.o_side:
                                new_position = (x+i, y+j)
                else:
                    new_position = self.pos
            self.model.grid.move_agent(self, new_position)
            self.calculate_side()

    def possible_positions(self):
        positions = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=False)
        positions_copy = positions.copy()
        for pos in positions_copy:
            if self.model.areas[pos] == self.o_side:
                positions.remove(pos)
        return positions

    def child_pos(self):
        positions = self.possible_positions()
        positions_copy = positions.copy()
        for pos in positions_copy:
            if self.model.areas[pos[0]][pos[1]] == 1:
                positions.remove(pos)
        if len(positions) == 0:
            pos = self.pos
        else:
            pos = self.random.choice(positions)
        return pos
