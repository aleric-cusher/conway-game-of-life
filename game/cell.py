from __future__ import annotations
from typing import List, Tuple, TYPE_CHECKING
from game.cell_states import CellStatus
from game.rules import Rules, StandardRules
if TYPE_CHECKING:
    from game.grid import Grid


class Cell:
    neighbour_offsets = [(row, col) for row in [-1, 0, 1] for col in [-1, 0, 1] if not (row == 0 and col == 0)]
    def __init__(self, location: Tuple[int, int], status: CellStatus = CellStatus.DEAD, rules: Rules = StandardRules):
        self._location = location
        self._status = status
        self.rules = rules
        self._life_evaluation = None
    
    def _get_neighbours(self, grid: List[List[Cell]]) -> List[Cell]:
        neighbours = []
        for i, j in self.neighbour_offsets:
            neighbour_row = self._location[0] + i
            neighbour_col = self._location[1] + j
            if 0 <= neighbour_row < len(grid) and 0 <= neighbour_col < len(grid[0]):
                neighbours.append(grid[neighbour_row][neighbour_col])
        return neighbours

    def get_state(self) -> CellStatus:
        return self._status

    def set_state(self, state: CellStatus) -> None:
        self._status = state
    
    def evaluate_life(self, grid: List[List[Cell]]) -> None:
        neighbours = self._get_neighbours(grid)
        alive_neighbours = sum([1 for neighbour in neighbours if neighbour.get_state() == CellStatus.ALIVE])
        self._life_evaluation = self.rules.apply_rules(self._status, alive_neighbours)
    
    def update_status(self) -> None:
        if self._life_evaluation is not None:
            self._status = self._life_evaluation
            self._life_evaluation = None