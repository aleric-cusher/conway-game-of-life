from typing import Tuple
import numpy as np
from scipy.signal import convolve2d
from game.cell import Cell


class Grid:
    def __init__(self, size: Tuple[int, int] = (30, 30), random_seed: bool = False) -> None:
        if random_seed:
            self._grid = np.random.choice(list(Cell), size=size)
        else:
            self._grid = np.full(size, Cell.DEAD)

    def get_grid(self) -> np.ndarray:
        return np.vectorize(lambda x: Cell(x))(self._grid)

        
            
        
