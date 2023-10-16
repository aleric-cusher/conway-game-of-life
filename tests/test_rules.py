import pytest
from game.rules import StandardRules
from game.cell_state import CellState


class TestStandardRules:
    rules = StandardRules()

    def test_overpopulation(self):
        assert self.rules.apply_rules(CellState.ALIVE, 4) == CellState.DEAD
        assert self.rules.apply_rules(CellState.ALIVE, 5) == CellState.DEAD
    
    def test_underpopulation(self):
        assert self.rules.apply_rules(CellState.ALIVE, 1) == CellState.DEAD
        assert self.rules.apply_rules(CellState.ALIVE, 0) == CellState.DEAD

    def test_survival(self):
        assert self.rules.apply_rules(CellState.ALIVE, 2) == CellState.ALIVE
        assert self.rules.apply_rules(CellState.ALIVE, 3) == CellState.ALIVE
    
    def test_birth(self):
        assert self.rules.apply_rules(CellState.DEAD, 3) == CellState.ALIVE