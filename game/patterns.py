


from typing import List, Tuple


class StillLifePatterns:
    @staticmethod
    def block(top_left_location: Tuple[int, int] = (0, 0)) -> Tuple[List[Tuple[int, int]], Tuple[int, int]]:
        offset_row, offset_col= top_left_location
        locations = [(0, 0), (0, 1), (1, 0), (1, 1)]
        updated_locations = [(i + offset_row, j + offset_col) for i, j in locations]
        return updated_locations

    @staticmethod
    def beehive(top_left_location: Tuple[int, int] = (0, 0)):
        offset_row, offset_col= top_left_location
        locations = [(0, 1), (0, 2), (1, 0), (1, 3), (2, 1), (2, 2)]
        updated_locations = [(i + offset_row, j + offset_col) for i, j in locations]
        return updated_locations
    

class OscillatorPatterns:
    @staticmethod
    def blinker(top_left_location: Tuple[int, int] = (0, 0)):
        offset_row, offset_col= top_left_location
        locations = [(0, 1), (1, 1), (2, 1)]
        updated_locations = [(i + offset_row, j + offset_col) for i, j in locations]
        return updated_locations