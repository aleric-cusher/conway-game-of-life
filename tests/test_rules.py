import pytest
from game.rules import StandardRules
from game.cell import Cell


class TestStandardRules:
    rules = StandardRules

    def test_overpopulation(self):
        assert self.rules.apply_rules(Cell.ALIVE, 4) == Cell.DEAD
        assert self.rules.apply_rules(Cell.ALIVE, 5) == Cell.DEAD
    
    def test_underpopulation(self):
        assert self.rules.apply_rules(Cell.ALIVE, 1) == Cell.DEAD
        assert self.rules.apply_rules(Cell.ALIVE, 0) == Cell.DEAD

    def test_survival(self):
        assert self.rules.apply_rules(Cell.ALIVE, 2) == Cell.ALIVE
        assert self.rules.apply_rules(Cell.ALIVE, 3) == Cell.ALIVE
    
    def test_birth(self):
        assert self.rules.apply_rules(Cell.DEAD, 3) == Cell.ALIVE