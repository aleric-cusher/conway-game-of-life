from typing import Tuple
from game.cell_states import CellStatus
from game.rules import Rules, StandardRules


class Cell:
    def __init__(self, location: Tuple[int, int], status: CellStatus = CellStatus.DEAD, rules: Rules = StandardRules):
        self._location = location
        self._status = status
        self.rules = rules
    
    def get_state(self):
        return self._status