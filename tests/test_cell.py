from game.cell import Cell, StandardCell
from game.cell_states import CellStatus
from game.rules import StandardRules
from game.grid import Grid

def test_cell_creation():
    location = (3, 3)
    cell = StandardCell(location)
    assert cell._location == location
    assert cell._state == CellStatus.DEAD
    assert isinstance(cell.rules, StandardRules)

def test_get_state():
    location = (3, 3)
    cell = StandardCell(location)
    assert cell.get_state() == CellStatus.DEAD

    cell.set_state(CellStatus.ALIVE)
    assert cell.get_state() == CellStatus.ALIVE
    
def test_evaluate_life():
    location = (0, 1)
    cell = StandardCell(location)
    grid = Grid((3, 3))
    grid._grid[0][1] = cell
    assert cell._life_evaluation == None
    cell.evaluate_life(grid.get_grid())
    assert cell._life_evaluation == CellStatus.DEAD

def test_update_state():
    location = (0, 1)
    cell = StandardCell(location)
    assert cell._state == CellStatus.DEAD
    cell._life_evaluation = CellStatus.ALIVE
    cell.update_state()
    assert cell._state == CellStatus.ALIVE