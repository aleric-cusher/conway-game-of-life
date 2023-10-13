from abc import ABC, abstractstaticmethod
from game.cell import Cell

class Rules(ABC):
    @abstractstaticmethod
    def apply_rules(cell: Cell, neighbours: int):
        pass

class StandardRules(Rules):
    @staticmethod
    def apply_rules(cell, neighbours):
        if cell == Cell.ALIVE:
            if neighbours == 2 or neighbours == 3:
                return Cell.ALIVE
            return Cell.DEAD
        if cell == Cell.DEAD:
            if neighbours == 3:
                return Cell.ALIVE
            return Cell.DEAD