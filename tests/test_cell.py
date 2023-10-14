from game.cell import StandardCell
from game.cell_states import CellStatus
from game.rules import StandardRules
from game.grid import Grid

def test_cell_creation():
    location = (3, 3)
    cell = StandardCell(location)
    assert cell._location == location
    assert cell._status == CellStatus.DEAD
    assert isinstance(cell.rules, StandardRules)

def test_get_status():
    location = (3, 3)
    cell = StandardCell(location)
    assert cell.get_state() == CellStatus.DEAD

    cell = StandardCell(location, status=CellStatus.ALIVE)
    assert cell.get_state() == CellStatus.ALIVE
    
def test_evaluate_life():
    location = (0, 1)
    cell = StandardCell(location)
    grid = Grid((3, 3))
    grid._grid[0][1] = cell
    assert cell._life_evaluation == None
    cell.evaluate_life(grid.get_grid())
    assert cell._life_evaluation == CellStatus.DEAD

def test_update_status():
    location = (0, 1)
    cell = StandardCell(location)
    assert cell._status == CellStatus.DEAD
    cell._life_evaluation = CellStatus.ALIVE
    cell.update_status()
    assert cell._status == CellStatus.ALIVE