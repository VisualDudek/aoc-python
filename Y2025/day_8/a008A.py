"""
"""
from dataclasses import dataclass
from typing import Dict, Generator, Protocol, List, Tuple, Union

type Point = Tuple[int, int, int]

def load_j_boxes(file_path: str) -> List[Point]:
    _boxes = []

    with open(file_path) as f:
        for row in f:
            x, y, z = map(int, row.strip().split(','))
            _boxes.append((x, y, z))

    return _boxes

class JBox:
    def __init__(self, position: Point) -> None:
        self.position = position
        self.member_of_circuit = False
        self.is_middle_box = False
        self.distance = None
        self.closest_neighbor: Union[None, 'JBox'] = None

    def get_closest_box(self, boxes: List["JBox"]) -> None:
        _tmp = []
        for box in boxes:
            if box is self:
                continue
            if box.is_middle_box:
                continue
            # compute Euclidean distance
            dist = ((self.position[0] - box.position[0]) ** 2 +
                    (self.position[1] - box.position[1]) ** 2 +
                    (self.position[2] - box.position[2]) ** 2) ** 0.5
            _tmp.append((dist, box))

        _tmp.sort(key=lambda x: x[0])
        self.distance, self.closest_neighbor = _tmp[0]

def main():
    file_path = "../puzzle_input/008_test.txt"
    # file_path = "../puzzle_input/008.txt"
    boxes = load_j_boxes(file_path)
    j_boxes = [JBox(position=box) for box in boxes]
    pass

    for box in j_boxes:
        box.get_closest_box(j_boxes)
        if box.closest_neighbor is not None:  # crazy mypy issue
            print(f"Box at {box.position} closest to {box.closest_neighbor.position} with distance {box.distance}")

    circuits = []

    for i in range(10):
        # find two boxes with lowest distance
        _tmp = [box for box in j_boxes if not box.is_middle_box]
        sorted_boxes = sorted(_tmp, key=lambda x: x.distance if x.distance is not None else float('inf'))
        box1 = sorted_boxes[0]
        box2 = box1.closest_neighbor


if __name__ == '__main__':
    main()