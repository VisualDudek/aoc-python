"""
- it is correct but do not like code flow
"""
from collections import deque
from typing import Dict, Tuple


type Point = Tuple[int, int]

class Beam:
    
    def __init__(self, position: Point) -> None:
        self.position = position

    # GOTCHA: instead of keeping position as tuple, you could have
    # Position class with x and y attributes and next_point property/method
    def drop_down(self) -> None:
        '''
        This method does not takes into account splitting
        '''
        x, y = self.position
        self.position = (x, y + 1)

    # GOTCHA: interesting approach is provide method next_beams with point of grid
    # that will determine if beam splits or not
    def next_beams(self, char: str) -> list['Beam']:
        x, y = self.position
        if char == '^':
            return [Beam((x - 1, y + 1)), Beam((x + 1, y + 1))]
        elif char == 'X':
            return []  # beam is lost
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


def main():
    file_path = "../puzzle_input/007_test.txt"
    # file_path = "../puzzle_input/007.txt"
    grid_dict = load_grid(file_path)
    # GOTCHA: could make Grid a class with methods to get neighbors, etc.
    grid = grid_dict

    # GOTCHA: this on-liner is crazy for starting point
    start_point = next(point for point, char in grid.items() if char == 'S')

    # beam_list = [Beam(start_point)]

    # --- trying to recover from previous fail ---
    beams  = deque([start_point])
    seen: set[Point] = set()  # GOTCHA: this syntax is interesting

    total_splitters = 0

    # GOTCHA: I can while on deque directly
    while beams:
        c_beam = beams.popleft()  # cSpell:words popleft

        next_beams = Beam(c_beam).next_beams(grid.get(c_beam, 'X'))
        for nb in next_beams:
            if nb.position not in seen:
                seen.add(nb.position)
                beams.append(nb.position)
        if len(next_beams) > 1:
            total_splitters += 1


    print(f"Total splitters encountered: {total_splitters}")


if __name__ == '__main__':
    main()

