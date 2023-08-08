from Agents.Cell import Cell


class T_naive_cell(Cell):
    def __init__(self, unique_id, model, proliferation_rate):
        super().__init__(unique_id, model, proliferation_rate)
        self.antigen_presented = None

    def step(self):
        self.move()
        self.proliferation()

    def myelin_reactive_activation(self):
        if self.antigen_presented == "Myelin":
            print()
