from typing import Tuple
import numpy as np


class Grid:
    def __init__(self, size: Tuple[int, int] = (30, 30), random_seed: bool = False) -> None:
        if random_seed:
            self._grid = np.random.randint(2, size=size, dtype=np.uint8)
        else:
            self._grid = np.zeros(size, dtype=np.uint8)
            
        
