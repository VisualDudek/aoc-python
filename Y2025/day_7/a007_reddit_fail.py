
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

    # find start point
    start_points = [point for point, char in grid.items() if char == 'S']
    if not start_points:
        raise ValueError("No start point 'S' found in the grid.")
    start_point = start_points[0]

    # GOTCHA: this on-liner is crazy for starting point
    start_point_gen = next(point for point, char in grid.items() if char == 'S')

    beam_list = [Beam(start_point)]

    max_y = max(y for _, y in grid.keys())

    total_splitters = 0

    # it should be `max_y + 1` to include last line


    # --- FAIL --- too much coupling here between grid and beam logic
    # get rid of for loop over and beam lists instead of deque
    seen = set()
    for y in range(max_y):
        new_beam_list = []
        for beam in beam_list:
            x,y = beam.position
            char = grid.get((x, y + 1), '.')
            beams_list = beam.next_beams(char)
            is_splitter = len(beams_list) > 1
            if is_splitter:
                total_splitters += 1
            new_beam_list.extend(beams_list)
        beam_list = new_beam_list

    print(f"Total splitters encountered: {total_splitters}")


if __name__ == '__main__':
    main()

