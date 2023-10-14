from abc import ABC, abstractstaticmethod
from game.cell_states import CellStatus

class Rules(ABC):
    @abstractstaticmethod
    def apply_rules(cell_status: CellStatus, neighbours: int):
        pass

class StandardRules(Rules):
    @staticmethod
    def apply_rules(cell_status, neighbours) -> None:
        if cell_status == CellStatus.ALIVE:
            if neighbours == 2 or neighbours == 3:
                return CellStatus.ALIVE
            return CellStatus.DEAD
        if cell_status == CellStatus.DEAD:
            if neighbours == 3:
                return CellStatus.ALIVE
            return CellStatus.DEAD