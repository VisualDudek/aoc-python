from dataclasses import dataclass
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


def process_one_line(grid: Grid, beam_list: List[Point], y: int) -> tuple[List[Point], int]:
    new_beam_list = []
    counter = 0

    # move beams down
    beam_moved_down = [(x, y + 1) for (x, y) in beam_list]
    
    splitters = [point for point in grid.grid.keys() if point[1] == y]
    for beam in beam_list:
        if beam in splitters:
            # split beam
            counter += 1
            # GOTCHA: what if beam is at edge of grid?
            new_beam_list.append((beam[0] - 1, beam[1] + 1))  # left
            new_beam_list.append((beam[0] + 1, beam[1] + 1))  # right
        else:
            new_beam_list.append((beam[0], beam[1] + 1))  # down

    return list(set(new_beam_list)), counter  # remove duplicates


def process_grid(grid: Grid) -> int:
    max_y = grid.get_max_y()
    start_point = grid.get_start_point()
    beam_list = [start_point]
    total_splits = 0

    for y in range(start_point[1], max_y+1):
        beam_list, splits = process_one_line(grid, beam_list, y)
        total_splits += splits

    return total_splits


def main():
    # file_path = "../puzzle_input/007_test.txt"
    file_path = "../puzzle_input/007.txt"
    grid_dict = load_grid(file_path)
    grid = Grid(grid_dict)
    pass

    total_splits = process_grid(grid)
    print(f"Total splits: {total_splits}")
    assert total_splits == 1592  # My Puzzle Input


if __name__ == '__main__':
    main()