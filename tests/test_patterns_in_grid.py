import pytest
from pprint import pprint
from game.grid import Grid
from game.patterns import StillLifePatterns, OscillatorPatterns

class TestStillLife:
    patterns = StillLifePatterns
    def test_block(self):
        grid = Grid((10, 10))
        alive_cells = self.patterns.block((2, 2))
        grid.add_cells(alive_cells)
        grid_snapshot = grid.get_grid()
        grid.step()
        assert grid.get_grid() == grid_snapshot

    def test_beehive(self):
        grid = Grid((10, 10))
        alive_cells = self.patterns.beehive((2, 2))
        grid.add_cells(alive_cells)
        grid_snapshot = grid.get_grid(True)
        pprint(grid_snapshot)
        grid.step()
        assert grid.get_grid(True) == grid_snapshot

class TestOscillator:
    patterns = OscillatorPatterns
    def test_blinker(self):
        grid = Grid((5, 5))
        alive_cells = self.patterns.blinker()
        grid.add_cells(alive_cells)
        assert grid.get_grid(True) ==  [[0, 1, 0, 0, 0],
                                        [0, 1, 0, 0, 0],
                                        [0, 1, 0, 0, 0],
                                        [0, 0, 0, 0, 0],
                                        [0, 0, 0, 0, 0]]
        grid.step()
        assert grid.get_grid(True) ==  [[0, 0, 0, 0, 0],
                                        [1, 1, 1, 0, 0],
                                        [0, 0, 0, 0, 0],
                                        [0, 0, 0, 0, 0],
                                        [0, 0, 0, 0, 0]]