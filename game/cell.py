from __future__ import annotations
from abc import ABC
from typing import List, Tuple
from game.cell_state import CellState
from game.location import Location
from game.rules import Rules, StandardRules


class Cell(ABC):
    def __init__(self, location: Location, rules: Rules, state: CellState = CellState.DEAD) -> None:
        self._location = location
        self._state = state
        self.rules = rules

    def set_state(self, state: CellState) -> None:
        self._state = state
    
    def evaluate_life(self, grid: List[List[Cell]]) -> None:
        neighbours = self._location.get_neighbours(grid)
        alive_neighbours = sum([1 for neighbour in neighbours if neighbour._state == CellState.ALIVE])
        self._state = self.rules.apply_rules(self._state, alive_neighbours)


class StandardCell(Cell):
    def __init__(self, location: Tuple[int, int]) -> None:
        super().__init__(location, rules=StandardRules())