from game.cell import StandardCell
from game.cell_state import CellState
from game.rules import StandardRules
from game.grid import Grid
from game.location import Location

def test_cell_creation():
    location = Location(3, 3)
    cell = StandardCell(location)
    assert cell._location == location
    assert cell._state == CellState.DEAD
    assert isinstance(cell.rules, StandardRules)

def test_get_state():
    location = Location(3, 3)
    cell = StandardCell(location)
    assert cell._state == CellState.DEAD

    cell.set_state(CellState.ALIVE)
    assert cell._state == CellState.ALIVE
    
def test_evaluate_life():
    location = Location(0, 1)
    cell = StandardCell(location)
    grid = Grid((3, 3))
    grid._grid[0][1] = cell
    cell.evaluate_life(grid.get_grid_snapshot())
    assert cell._state == CellState.DEAD
