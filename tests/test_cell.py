from game.cell import Cell

def test_cell():
    assert Cell.ALIVE in Cell
    assert Cell.DEAD in Cell