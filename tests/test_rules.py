import pytest
from game.rules import StandardRules
from game.cell_states import CellStatus


class TestStandardRules:
    rules = StandardRules

    def test_overpopulation(self):
        assert self.rules.apply_rules(CellStatus.ALIVE, 4) == CellStatus.DEAD
        assert self.rules.apply_rules(CellStatus.ALIVE, 5) == CellStatus.DEAD
    
    def test_underpopulation(self):
        assert self.rules.apply_rules(CellStatus.ALIVE, 1) == CellStatus.DEAD
        assert self.rules.apply_rules(CellStatus.ALIVE, 0) == CellStatus.DEAD

    def test_survival(self):
        assert self.rules.apply_rules(CellStatus.ALIVE, 2) == CellStatus.ALIVE
        assert self.rules.apply_rules(CellStatus.ALIVE, 3) == CellStatus.ALIVE
    
    def test_birth(self):
        assert self.rules.apply_rules(CellStatus.DEAD, 3) == CellStatus.ALIVE