from typing import Tuple
import numpy as np
from scipy.signal import convolve2d
from game.cell import Cell
from game.rules import StandardRules, Rules


class Grid:
    def __init__(self, size: Tuple[int, int] = (30, 30), random_seed: bool = False, rules: Rules = StandardRules) -> None:
        if not issubclass(rules, Rules):
            raise TypeError('Parameter: rules should be of the type Rules')

        if random_seed:
            self._grid = np.random.choice(list(Cell), size=size)
        else:
            self._grid = np.full(size, Cell.DEAD)
        
        self.rules = rules

    def _get_primitive_grid(self) -> np.ndarray[int]:
        return np.vectorize(lambda x: x.value)(self._grid)

    def get_grid(self) -> np.ndarray[Cell]:
        return np.copy(self._grid)

    def step(self) -> None:
        padded_grid = np.pad(self._get_primitive_grid(), pad_width=1, mode='constant')
        mask = np.array([
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ])

        neighbours = convolve2d(padded_grid, mask, mode='valid')

        new_grid = np.full(self._grid.shape, Cell.DEAD)
        for i in range(self._grid.shape[0]):
            for j in range(self._grid.shape[1]):
                new_grid[i, j] = self.rules.apply_rules(self._grid[i, j], neighbours[i, j])

        self._grid = new_grid
        
            
        
