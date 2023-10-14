from typing import List, Tuple
import random
from game.cell import Cell
from game.cell_states import CellStatus


class Grid:
    def __init__(self, size: Tuple[int, int] = (30, 30), random_seed: bool = False, live_cell_locations: List[Tuple[int, int]] = None) -> None:
        self._grid: List[Cell] = []
        for i in range(size[0]):
            row = []
            for j in range(size[1]):
                if live_cell_locations is not None and (i, j) in live_cell_locations:
                    cell = Cell((i,j), status=CellStatus.ALIVE)
                else:
                    cell = Cell((i, j), status=random.choice(list(CellStatus)) if random_seed else CellStatus.DEAD)
                row.append(cell)
            self._grid.append(row)
    