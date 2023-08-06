import mesa

from mesa.model import Model


class Virus(mesa.Agent):
    def __init__(self, unique_id: int, model: Model):
        super().__init__(unique_id, model)
        self.health = 1

    def step(self):
        self.move()

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=False)
        if self.model.areas[self.pos[0]][self.pos[1]] in [1, 2]:
            for pos in possible_steps:
                if self.model.areas[pos[0]][pos[1]] != 2:
                    possible_steps.remove(pos)
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)
