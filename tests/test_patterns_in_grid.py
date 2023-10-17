import pytest
from pprint import pprint
from game.grid import Grid
from game.patterns import StillLifePatterns, OscillatorPatterns

class TestStillLife:
    patterns = StillLifePatterns
    def test_block(self):
        alive_cells = self.patterns.block((2, 2))
        grid = Grid((10, 10), live_cell_locations=alive_cells)
        grid_snapshot = grid.get_grid_snapshot()
        grid.step()
        new_snapshot = grid.get_grid_snapshot()
        for i in range(10):
            for j in range(10):
                assert grid_snapshot[i][j]._state == new_snapshot[i][j]._state

    def test_beehive(self):
        alive_cells = self.patterns.beehive((2, 2))
        grid = Grid((10, 10), live_cell_locations=alive_cells)
        grid_snapshot = grid.get_grid_snapshot()
        grid.step()
        new_snapshot = grid.get_grid_snapshot()
        for i in range(10):
            for j in range(10):
                assert grid_snapshot[i][j]._state == new_snapshot[i][j]._state

class TestOscillator:
    patterns = OscillatorPatterns
    def test_blinker(self):
        alive_cells = self.patterns.blinker()
        grid = Grid((5, 5), live_cell_locations=alive_cells)
        snapshot = grid.get_grid_snapshot()
        snapshot = [[cell._state.value for cell in row] for row in snapshot]

        assert snapshot == [[0, 1, 0, 0, 0],
                            [0, 1, 0, 0, 0],
                            [0, 1, 0, 0, 0],
                            [0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0]]
        
        grid.step()
        snapshot = grid.get_grid_snapshot()
        snapshot = [[cell._state.value for cell in row] for row in snapshot]
        assert snapshot == [[0, 0, 0, 0, 0],
                            [1, 1, 1, 0, 0],
                            [0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0]]