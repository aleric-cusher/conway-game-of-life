import pytest
from game.grid import Grid
from game.location import Location

def test_location_creation():
    location = Location(3, 5)
    assert location.row == 3
    assert location.col == 5

def test_is_valid():
    location = Location(1, 5)
    grid = [[1, 2], [3, 4]]
    assert location.is_valid(grid) == False

    location = Location(1, 0)
    assert location.is_valid(grid) == True

def test_get_neighbours():
    location = Location(0, 0)
    grid = Grid((3, 3))
    neighbours = location.get_neighbours(grid.get_grid_snapshot())
    neighbour_locations = [Location(i, j) for j in range(2) for i in range(2)]
    for neighbour in neighbours:
        location = neighbour._location
        assert location in neighbour_locations

def test_add_coordinates():
    location = Location(3, 4)
    new_location = location + (2, 1)

    assert new_location.row == 5
    assert new_location.col == 5

def test_equality_equals():
    location = Location(2, 3)
    other_location = Location(2, 3)

    assert location == other_location

def test_equality_not_equals():
    location = Location(2, 3)
    other_location = Location(5, 3)

    assert (location == other_location) == False
