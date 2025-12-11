"""
"""
from collections import deque, Counter
from typing import Dict, List, Tuple


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
        

def load_grid(file_path: str) -> Tuple[str, int, List[str]]:
    

    with open(file_path) as f:
        first_line, *lines = f.readlines()
        start = first_line.index('S')

    return first_line.strip(), start, [line.strip() for line in lines]



def main():
    # file_path = "../puzzle_input/007_test.txt"
    file_path = "../puzzle_input/007.txt"
    first_row, start, lines = load_grid(file_path)

    num_splits = 0
    timelines = [0] * len(first_row)
    timelines[start] = 1  # start with one timeline at the start position

    for line in lines:
        for col, char in enumerate(line):
            # The timeline will only split if there is a splitter '^' at that position
            if not (char == '^' and timelines[col] > 0):
                continue

            num_splits += 1
            # Slit the timelines to left and right
            timelines[col - 1] += timelines[col]
            timelines[col + 1] += timelines[col]

            # No timelines will continue in this column
            # HACK This overwrites beams in the case of two adjacent splitters,
            # but that's okay because that never happens in the input
            timelines[col] = 0 # because of '^' in this column

    print(f"Total splitters encountered: {num_splits}")
    print(f"Total timelines reaching bottom row: {sum(timelines)}")

if __name__ == '__main__':
    main()

