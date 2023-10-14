from copy import copy
from typing import List, Tuple, Union
import random
from game.cell import Cell
from game.cell_states import CellStatus


class Grid:
    def __init__(self, size: Tuple[int, int] = (30, 30), random_seed: bool = False, live_cell_locations: List[Tuple[int, int]] = None) -> None:
        self._grid: List[List[Cell]] = []
        for i in range(size[0]):
            row = []
            for j in range(size[1]):
                if live_cell_locations is not None and (i, j) in live_cell_locations:
                    cell = Cell((i,j), status=CellStatus.ALIVE)
                else:
                    cell = Cell((i, j), status=random.choice(list(CellStatus)) if random_seed else CellStatus.DEAD)
                row.append(cell)
            self._grid.append(row)

        self.size = size
    
    def get_grid(self, primitive_array: bool = False) -> Union[List[List[Cell]], List[List[int]]]:
        if not primitive_array:
            return copy(self._grid)
        return [[cell.get_state().value for cell in row] for row in self._grid]
        
    def step(self) -> List[List[CellStatus]]:
        grid = self.get_grid()
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                self._grid[i][j].evaluate_life(grid)
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                self._grid[i][j].update_status()

        return self.get_grid()
        