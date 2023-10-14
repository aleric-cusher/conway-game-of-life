from game.cell import Cell
from game.cell_states import CellStatus
from game.rules import StandardRules

def test_cell_creation():
    location = (3, 3)
    cell = Cell(location)
    assert cell._location == location
    assert cell._status == CellStatus.DEAD
    assert cell.rules == StandardRules

def test_get_status():
    location = (3, 3)
    cell = Cell(location)
    assert cell.get_state() == CellStatus.DEAD

    cell = Cell(location, status=CellStatus.ALIVE)
    assert cell.get_state() == CellStatus.ALIVE
    