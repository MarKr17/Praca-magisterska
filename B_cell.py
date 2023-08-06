from Cell import Cell


class B_cell(Cell):
    def __init__(self, unique_id, model, proliferation_rate):
        super().__init__(unique_id, model, proliferation_rate)

    def step(self):
        self.move()
        self.proliferation()
        if self.health <= 0:
            self.death()
