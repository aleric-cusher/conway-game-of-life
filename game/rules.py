from abc import ABC
from typing import List, Tuple
from game.cell_state import CellState

class Rules(ABC):
    def __init__(self, rule_string: str) -> None:
        self.birth, self.survival = self._parse_rulestring(rule_string)

    def _parse_rulestring(self, rule_string: str) -> Tuple[List[int], List[int]]:
        str1, str2 = rule_string.split('/')
        if 'B' in str1:
            birth = str1.replace('B', '')
            survival = str2.replace('S', '')
        else:
            birth = str2.replace('B', '')
            survival = str1.replace('S', '')
        
        birth = list(map(int, list(birth)))
        survival = list(map(int, list(survival)))
        return birth, survival

    def apply_rules(self, cell_status: CellState, num_neighbours: int) -> CellState:
        if cell_status == CellState.DEAD and num_neighbours in self.birth:
            return CellState.ALIVE
        if cell_status == CellState.ALIVE and num_neighbours in self.survival:
            return CellState.ALIVE
        return CellState.DEAD


class StandardRules(Rules):
    def __init__(self) -> None:
        super().__init__('B3/S23')