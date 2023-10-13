import pytest
from numpy import random
from game.grid import Grid


def test_grid_creation():
    size = (25, 30)
    grid = Grid(size)
    assert grid._grid.shape == size

def test_grid_creation_random(mocker):
    size = (3, 4)
    spy = mocker.spy(random, 'randint')
    grid = Grid(size, random_seed=True)
    assert grid._grid.shape == size
    assert spy.call_count == 1

def test_grid_invalid_size():
    size = 'a', 'b'
    with pytest.raises(TypeError):
        grid = Grid(size)