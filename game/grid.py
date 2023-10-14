from copy import copy
from typing import List, Tuple, Union
import random
from game.cell import Cell
from game.cell_states import CellStatus


class Grid:
    def __init__(self, size: Tuple[int, int] = (30, 30), random_seed: bool = False, live_cell_locations: List[Tuple[int, int]] = None) -> None:
        self.size = size
        self._grid: List[List[Cell]] = [[Cell((i, j)) for j in range(size[1])] for i in range(size[0])]
        self.all_indices = [(i, j) for j in range(size[1]) for i in range(size[0])]

        if random_seed:
            locations = [(i, j) for i, j in self.all_indices if random.choice([0, 1]) == 1]
            self.add_cells(locations)

        if live_cell_locations is not None:
            self.add_cells(live_cell_locations)
    
    def add_cells(self, cell_locations: List[Tuple[int, int]], cell_status: CellStatus = CellStatus.ALIVE) -> None:
        for i, j in cell_locations:
            self._grid[i][j].set_state(cell_status)
    
    def get_grid(self, primitive_array: bool = False) -> Union[List[List[Cell]], List[List[int]]]:
        if not primitive_array:
            return copy(self._grid)
        return [[cell.get_state().value for cell in row] for row in self._grid]
        
    def step(self) -> None:
        grid = self.get_grid()
        for i, j in self.all_indices:
            self._grid[i][j].evaluate_life(grid)

        for i, j in self.all_indices:
                self._grid[i][j].update_status()
