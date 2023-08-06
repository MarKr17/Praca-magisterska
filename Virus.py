import mesa

from mesa.model import Model


class Virus(mesa.Agent):
    def __init__(self, unique_id: int, model: Model):
        super().__init__(unique_id, model)
        self.health = 1
        self.placement = 0

    def step(self):
        self.move()

    def move(self):
        positions = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=False)
        positions_copy = positions.copy()
        for pos in positions_copy:
            a = self.model.areas[pos[0]][pos[1]]
            if a == 1 or a == 2:
                positions.remove(pos)
        new_position = self.random.choice(positions)
        self.model.grid.move_agent(self, new_position)
