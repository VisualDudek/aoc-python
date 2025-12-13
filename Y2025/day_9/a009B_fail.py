"""
Day 9: Part 2
- trying to use grid based approach, implement method to fill the area inside
"""
from dataclasses import dataclass
from typing import Dict, Generator, Protocol, List, Tuple, Union
from itertools import combinations
from math import dist, prod
from typing import NamedTuple

class Point(NamedTuple):
    x: int
    y: int

def load(file_path: str) -> List[Point]:
    _points = []

    with open(file_path) as f:
        for row in f:
            x, y = map(int, row.strip().split(','))
            _points.append(Point(x, y))

    return _points

class Grid:
    def __init__(self, points: List[Point]):
        self.points = points
        self.max_x = max(p[0] for p in points)
        self.max_y = max(p[1] for p in points)
        self.min_x = min(p[0] for p in points) 
        self.min_y = min(p[1] for p in points)  
        self.green_points: set[Point] = set(points)

        self._post_init()


    def _post_init(self) -> None:
        # Initialize grid based on points
        pairs = zip(self.points, self.points[1:]+[self.points[0]])
        for p1, p2 in pairs:
            # Draw lines between points
            if p1.x == p2.x: # vertical line
                for y in range(min(p1.y, p2.y), max(p1.y, p2.y)+1):
                    self.green_points.add(Point(p1.x, y))
            elif p1.y == p2.y: # horizontal line
                for x in range(min(p1.x, p2.x), max(p1.x, p2.x)+1):
                    self.green_points.add(Point(x, p1.y))

        # --- FAILING PART ---
        # ~9.3 billion iterations for real input, too slow
        # --------------------
        # Draw filled area - naive approach
        for y in range(self.min_y, self.max_y+1):
            in_area = False
            for x in range(self.min_x, self.max_x+1):
                pt = Point(x, y)
                # GOTCHA: Below if was tricky to get right
                if pt in self.green_points and Point(x+1, y) not in self.green_points:
                    in_area = not in_area
                elif in_area:
                    self.green_points.add(pt)


    def draw(self):
        for y in range(self.min_y, self.max_y+1):
            row = ''
            for x in range(self.min_x, self.max_x+1):
                if Point(x, y) in self.green_points:
                    row += '#'
                else:
                    row += '.'
            print(row)


def calc_area(p1: Point, p2: Point) -> int:
    return (abs(p1[0] - p2[0])+1) * (abs(p1[1] - p2[1]) + 1)


def is_overlay(p1: Point, p2: Point, grid: Grid) -> bool:
    does_overlay = True
    for x in range(min(p1.x, p2.x), max(p1.x, p2.x)+1):
        for y in range(min(p1.y, p2.y), max(p1.y, p2.y)+1):
            if Point(x, y) not in grid.green_points:
                return False
    return does_overlay


def main():
    # file_path = "../puzzle_input/009_test.txt"
    file_path = "../puzzle_input/009.txt"
    points: List[Point] = load(file_path)
    grid = Grid(points)
    # grid.draw()

    pairs = combinations(points, 2)
    from math import comb
    no = comb(len(points), 2)

    # check which pairs overlay green area
    overlaying_pairs = []
    for i, (p1, p2) in enumerate(pairs):
        print(f"Checking pair {i+1} out of {no}")
        if is_overlay(p1, p2, grid):
            overlaying_pairs.append((p1, p2))

    # find max area among overlaying pairs
    res_part2 = max(calc_area(p1, p2) for p1, p2 in overlaying_pairs)

    print(f"Result Part 2: {res_part2}")


if __name__ == '__main__':
    main()