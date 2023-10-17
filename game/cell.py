from __future__ import annotations
from abc import ABC
from typing import List, Tuple
from game.cell_state import CellState
from game.location import Location
from game.rules import Rules, StandardRules


class Cell(ABC):
    neighbour_offsets = [(row, col) for row in [-1, 0, 1] for col in [-1, 0, 1] if not (row == 0 and col == 0)]

    def __init__(self, location: Location, rules: Rules, state: CellState = CellState.DEAD) -> None:
        self._location = location
        self._state = state
        self.rules = rules
    
    def _get_neighbours(self, grid: List[List[Cell]]) -> List[Cell]:
        neighbours = []
        for i, j in self.neighbour_offsets:
            neighbour = self._location + (i, j)
            if neighbour.is_valid(grid):
                neighbours.append(grid[neighbour.row][neighbour.col])
        return neighbours

    def set_state(self, state: CellState) -> None:
        self._state = state
    
    def evaluate_life(self, grid: List[List[Cell]]) -> None:
        neighbours = self._get_neighbours(grid)
        alive_neighbours = sum([1 for neighbour in neighbours if neighbour._state == CellState.ALIVE])
        self._state = self.rules.apply_rules(self._state, alive_neighbours)


class StandardCell(Cell):
    def __init__(self, location: Tuple[int, int]) -> None:
        super().__init__(location, rules=StandardRules())