
from typing import Dict, Tuple


type Point = Tuple[int, int]

class Beam:
    
    def __init__(self, position: Point) -> None:
        self.position = position

    # GOTCHA: instead of keeping position as tuple, you could have
    # Position class with x and y attributes and next_point property/method
    def drop_down(self) -> None:
        x, y = self.position
        self.position = (x, y + 1)

    # GOTCHA: interesting approach is provide method next_beams with point of grid
    # that will determine if beam splits or not
    def next_beams(self, is_splitter: bool) -> list['Beam']:
        x, y = self.position
        if is_splitter:
            return [Beam((x - 1, y + 1)), Beam((x + 1, y + 1))]
        else:
            return [Beam((x, y + 1))]
        

def load_grid(file_path: str) -> Dict[Point, str]:
    _grid = {}

    with open(file_path) as f:
        for y, line in enumerate(f):
            for x, char in enumerate(line.strip()):
                # GOTCHA: decision to skip '.' here was stupid BC
                # later you need to check if point is in grid
                # if char != '.':
                _grid[(x, y)] = char

    return _grid

