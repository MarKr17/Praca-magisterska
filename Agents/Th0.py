from Agents.Cell import Cell
import random


class Th0(Cell):
    def __init__(self, unique_id, model, proliferation_rate):
        super().__init__(unique_id, model, proliferation_rate)
        self.antigen_attached = ''
