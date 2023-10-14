


from typing import List, Tuple


class StillLifePatterns:
    @staticmethod
    def block(top_left_location: Tuple[int, int] = (0, 0)) -> Tuple[List[Tuple[int, int]], Tuple[int, int]]:
        offset_row, offset_col= top_left_location
        height, width = 2, 2
        locations = [(0, 0), (0, 1), (1, 0), (1, 1)]
        updated_locations = [(i + offset_row, j + offset_col) for i, j in locations]
        return updated_locations, (height, width)

    @staticmethod
    def beehive(top_left_location: Tuple[int, int] = (0, 0)):
        offset_row, offset_col= top_left_location
        height, width = 3, 4
        locations = [(0, 1), (0, 2), (1, 0), (1, 3), (2, 1), (2, 2)]
        updated_locations = [(i + offset_row, j + offset_col) for i, j in locations]
        return updated_locations, (height, width)
    

class OscillatorPatterns:
    @staticmethod
    def blinker(top_left_location: Tuple[int, int] = (0, 0), state: int = 0):
        offset_row, offset_col= top_left_location
        height, width = 3, 3
        if state == 0:
            locations = [(0, 1), (1, 1), (2, 1)]
        else:
            locations = [(1, 0), (1, 1), (1, 2)]
        updated_locations = [(i + offset_row, j + offset_col) for i, j in locations]
        return updated_locations, (height, width)