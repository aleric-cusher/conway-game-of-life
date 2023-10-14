import pytest
from game.patterns import StillLifePatterns, OscillatorPatterns

class TestStillLifePatterns:
    patterns = StillLifePatterns
    def test_block(self):
        live_cells = self.patterns.block((1, 0))
        assert live_cells == [(1, 0), (1, 1), (2, 0), (2, 1)]
    
    def test_beehive(self):
        live_cells = self.patterns.beehive()
        assert live_cells == [(0, 1), (0, 2), (1, 0), (1, 3), (2, 1), (2, 2)]


class TestOscillatorPatterns:
    patterns = OscillatorPatterns
    def test_blinker(self):
        live_cells = self.patterns.blinker()
        assert live_cells == [(0, 1), (1, 1), (2, 1)]