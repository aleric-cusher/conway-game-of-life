from game.cell_state import CellState

def test_status_alive():
    assert CellState.ALIVE in CellState

def test_status_dead():
    assert CellState.DEAD in CellState
    