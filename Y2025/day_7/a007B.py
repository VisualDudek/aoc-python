"""
- ont sure if this is the best way to do this...
- could make Grid a dataclass with methods to get neighbors, etc.
- could make Beam a class with position and direction ???
- can I subclass dict to make Grid? and avoid code `grid.grid` ?
"""
from dataclasses import dataclass
from functools import lru_cache
from typing import Dict, Generator, Protocol, List, Tuple

type Point = Tuple[int, int]

# TODO: grid should be dataclass with methods to get neighbors, etc.

def load_grid(file_path: str) -> Dict[Point, str]:
    _grid = {}

    with open(file_path) as f:
        for y, line in enumerate(f):
            for x, char in enumerate(line.strip()):
                if char != '.':
                    _grid[(x, y)] = char

    return _grid


@dataclass
class Grid:
    grid: Dict[Point, str]

    def get_start_point(self) -> Point:
        start_points = [point for point, char in self.grid.items() if char == 'S']
        if not start_points:
            raise ValueError("No start point 'S' found in the grid.")
        return start_points[0]
    
    def get_max_y(self) -> int:
        if not self.grid:
            return 0
        return max(y for _, y in self.grid.keys())


def process_one_line(grid: Grid, beam_list: List[Point], y: int) -> List[Point]:
    new_beam_list = []

    print(f"Processing line y={y} with no. of beams: {len(beam_list)}")

    # move beams down
    # not needed anymore bc beams are moved when added to new_beam_list
    beam_moved_down = [(x, y + 1) for (x, y) in beam_list]
    
    splitters = tuple(point for point in grid.grid.keys() if point[1] == y)
    for beam in beam_list:
        # TODO: refactor to function
        # if beam in splitters:
        #     # split beam
        #     # GOTCHA: what if beam is at edge of grid?
        #     new_beam_list.append((beam[0] - 1, beam[1] + 1))  # left
        #     new_beam_list.append((beam[0] + 1, beam[1] + 1))  # right
        # else:
        #     new_beam_list.append((beam[0], beam[1] + 1))  # down

        new_beam_list.extend(helper(beam, splitters, y))

    print(f"Processed line y={y} with no. of beams: {len(new_beam_list)}")

    return new_beam_list

# GOTCHA: lru_cache needs hashable args
# GOTCHA: cache wont help you here, need different approach
@lru_cache(maxsize=None)
def helper(beam: Point, splitters: tuple[Point], y: int) -> List[Point]:
    new_beam_list = []
    if beam in splitters:
        # split beam
        # GOTCHA: what if beam is at edge of grid?
        new_beam_list.append((beam[0] - 1, beam[1] + 1))  # left
        new_beam_list.append((beam[0] + 1, beam[1] + 1))  # right
    else:
        new_beam_list.append((beam[0], beam[1] + 1))  # down
    return new_beam_list


def process_grid(grid: Grid) -> int:
    max_y = grid.get_max_y()
    start_point = grid.get_start_point()
    beam_list = [start_point]

    for y in range(start_point[1], max_y+1):
        beam_list = process_one_line(grid, beam_list, y)
        
    return len(beam_list)


def main():
    # file_path = "../puzzle_input/007_test.txt"
    file_path = "../puzzle_input/007.txt"
    grid_dict = load_grid(file_path)
    grid = Grid(grid_dict)
    pass

    total_splits = process_grid(grid)
    print(f"Total timelines/beams: {total_splits}")
    # assert total_splits == 40  # Test Input
    # assert total_splits == ???  # My Puzzle Input


if __name__ == '__main__':
    main()