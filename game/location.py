from __future__ import annotations
from typing import List, Tuple


class Location:
    def __init__(self, row: int, col: int) -> None:
        self.row = row
        self.col = col

    def is_valid(self, grid: List[List]) -> bool:
        return 0 <= self.row < len(grid) and 0 <= self.col < len(grid[0])
    
    def __add__(self, coordinates: Tuple[int, int]) -> Location:
        row, col = self.row + coordinates[0], self.col + coordinates[1]
        return Location(row, col)

    def __eq__(self, other_location: Location) -> bool:
        return self.row == other_location.row and self.col == other_location.col