import pytest
from game.patterns import StillLifePatterns, OscillatorPatterns

class TestStillLifePatterns:
    patterns = StillLifePatterns
    def test_block(self):
        live_cells, (height, width) = self.patterns.block((1, 0))
        assert height == 2
        assert width == 2
        assert live_cells == [(1, 0), (1, 1), (2, 0), (2, 1)]
    
    def test_beehive(self):
        live_cells, (height, width) = self.patterns.beehive()
        assert height == 3
        assert width == 4
        assert live_cells == [(0, 1), (0, 2), (1, 0), (1, 3), (2, 1), (2, 2)]


class TestOscillatorPatterns:
    patterns = OscillatorPatterns
    def test_blinker(self):
        live_cells, (height, width) = self.patterns.blinker()
        assert height == 3
        assert width == 3
        assert live_cells == [(0, 1), (1, 1), (2, 1)]

        live_cells, (height, width) = self.patterns.blinker(state=1)
        assert live_cells == [(1, 0), (1, 1), (1, 2)]