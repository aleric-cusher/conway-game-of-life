import pytest
from numpy import random
from game.cell import Cell
from game.grid import Grid


def test_grid_creation():
    size = (25, 30)
    grid = Grid(size)
    assert grid._grid.shape == size

def test_grid_creation_random(mocker):
    size = (3, 4)
    spy = mocker.spy(random, 'choice')
    grid = Grid(size, random_seed=True)
    assert grid._grid.shape == size
    assert spy.call_count == 1

def test_grid_invalid_size():
    size = 'a', 'b'
    with pytest.raises(TypeError):
        grid = Grid(size)

def test_get_grid():
    grid = Grid((3, 4), random_seed=True)
    canvas = grid.get_grid()
    for each in canvas.reshape(canvas.shape[0]*canvas.shape[1]):
        assert each in Cell
    