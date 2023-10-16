import pytest
import random
from game.cell_state import CellState
from game.grid import Grid

def test_grid_creation():
    size = (25, 30)
    grid = Grid(size)
    assert len(grid._grid) == size[0]
    assert len(grid._grid[0]) == size[1]
    for i in range(size[0]):
        for j in range(size[1]):
            assert grid._grid[i][j].get_state() == CellState.DEAD

def test_grid_creation_random(mocker):
    size = (25, 30)
    spy = mocker.spy(random, 'choice')
    grid = Grid(size, random_seed=True)
    assert len(grid._grid) == size[0]
    assert len(grid._grid[0]) == size[1]
    assert spy.call_count == size[0] * size[1]

def test_grid_creation_with_alive_cells():
    size = (5, 5)
    grid = Grid(size, live_cell_locations=[(2, 2), (3, 4)])
    grid._grid[2][2].get_state() == CellState.ALIVE
    grid._grid[3][4].get_state() == CellState.ALIVE

def test_get_grid():
    size = (5, 5)
    grid = Grid(size, live_cell_locations=[(2, 2), (3, 4)])
    gotten_grid = grid.get_grid_snapshot()
    for i in range(5):
        for j in range(5):
            assert gotten_grid[i][j].get_state() == grid._grid[i][j].get_state()

def test_get_grid_primitive():
    size = (2, 2)
    grid = Grid(size, live_cell_locations=[(1, 1)])
    expected_grid = [[0, 0], [0, 1]]
    gotten_grid = grid.get_grid_snapshot(primitive_array=True)
    assert gotten_grid == expected_grid

def test_step():
    size = (5, 5)
    grid = Grid(size, live_cell_locations=[(1, 1)])
    grid.step()
    grid_array = grid.get_grid_snapshot()
    for i in range(size[0]):
        for j in range(size[1]):
            assert grid_array[i][j].get_state() == CellState.DEAD
