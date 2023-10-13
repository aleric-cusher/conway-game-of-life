from game.cell_states import CellStatus

def test_status_alive():
    assert CellStatus.ALIVE in CellStatus

def test_status_dead():
    assert CellStatus.DEAD in CellStatus
    