"""
Day 9: Part 1
"""
from dataclasses import dataclass
from typing import Dict, Generator, Protocol, List, Tuple, Union
from itertools import combinations
from math import dist, prod

type Point = Tuple[int, int, int]

def load(file_path: str) -> List[Point]:
    _points = []

    with open(file_path) as f:
        for row in f:
            x, y = map(int, row.strip().split(','))
            _points.append((x, y))

    return _points

def calc_area(p1: Point, p2: Point) -> int:
    return (abs(p1[0] - p2[0])+1) * (abs(p1[1] - p2[1]) + 1)


def main():
    # file_path = "../puzzle_input/009_test.txt"
    file_path = "../puzzle_input/009.txt"
    points: List[Point] = load(file_path)

    pairs = combinations(points, 2)

    res_part1 = max(calc_area(p1, p2) for p1, p2 in pairs)

    print(f"Result Part 1: {res_part1}")



if __name__ == '__main__':
    main()