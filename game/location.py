from __future__ import annotations
from typing import List, Tuple, TYPE_CHECKING
if TYPE_CHECKING:
    from game.cell import Cell


class Location:
    neighbour_offsets = [(row, col) for row in [-1, 0, 1] for col in [-1, 0, 1] if not (row == 0 and col == 0)]

    def __init__(self, row: int, col: int) -> None:
        self.row = row
        self.col = col

    def get_neighbours(self, grid: List[List[Cell]]) -> List[Cell]:
        neighbours = []
        for i, j in self.neighbour_offsets:
            neighbour_coordinates = self + (i, j)
            if neighbour_coordinates.is_valid(grid):
                neighbours.append(grid[neighbour_coordinates.row][neighbour_coordinates.col])
        return neighbours

    def is_valid(self, grid: List[List]) -> bool:
        return 0 <= self.row < len(grid) and 0 <= self.col < len(grid[0])
    
    def __add__(self, coordinates: Tuple[int, int]) -> Location:
        row, col = self.row + coordinates[0], self.col + coordinates[1]
        return Location(row, col)

    def __eq__(self, other_location: Location) -> bool:
        return self.row == other_location.row and self.col == other_location.col