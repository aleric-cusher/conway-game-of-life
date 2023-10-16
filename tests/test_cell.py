from game.cell import Cell, StandardCell
from game.cell_state import CellState
from game.rules import StandardRules
from game.grid import Grid

def test_cell_creation():
    location = (3, 3)
    cell = StandardCell(location)
    assert cell._location == location
    assert cell._state == CellState.DEAD
    assert isinstance(cell.rules, StandardRules)

def test_get_state():
    location = (3, 3)
    cell = StandardCell(location)
    assert cell.get_state() == CellState.DEAD

    cell.set_state(CellState.ALIVE)
    assert cell.get_state() == CellState.ALIVE
    
def test_evaluate_life():
    location = (0, 1)
    cell = StandardCell(location)
    grid = Grid((3, 3))
    grid._grid[0][1] = cell
    cell.evaluate_life(grid.get_grid_snapshot())
    assert cell._state == CellState.DEAD
