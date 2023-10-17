from copy import deepcopy
from typing import List, Tuple, Type
import random
from game.cell import Cell, StandardCell
from game.cell_state import CellState
from game.location import Location


class Grid:
    def __init__(self, size: Tuple[int, int] = (30, 30), random_seed: bool = False, live_cell_locations: List[Tuple[int, int]] | None = None, cell_class: Type[Cell] = StandardCell) -> None:
        self.size = size
        self._grid: List[List[Cell]] = [[cell_class(Location(i, j)) for j in range(size[1])] for i in range(size[0])]
        self.all_indices = [Location(i, j) for j in range(size[1]) for i in range(size[0])]

        self._initialize_grid(random_seed, live_cell_locations)
        
    def _initialize_grid(self, random_seed: bool, live_cell_locations: List[Location]) -> None:
        if random_seed:
            locations = [location for location in self.all_indices if random.choice([True, False])]
            self._add_cells(locations)

        if live_cell_locations is not None:
            live_cell_locations = [Location(i, j) for i, j in live_cell_locations]
            self._add_cells(live_cell_locations)
    
    def _add_cells(self, cell_locations: List[Location], cell_status: CellState = CellState.ALIVE) -> None:
        for location in cell_locations:
            self._grid[location.row][location.col].set_state(cell_status)
    
    def get_grid_snapshot(self) -> List[List[Cell]] | List[List[int]]:
        return deepcopy(self._grid)
        
    def step(self) -> None:
        grid = self.get_grid_snapshot()
        for location in self.all_indices:
            self._grid[location.row][location.col].evaluate_life(grid)
