from typing import Dict, Protocol, List, Tuple

type Data = Dict[Tuple[int,int], bool]

class Solver(Protocol):
    def solve(self, data: Data) -> int:
        ...

class Loader(Protocol):
    def load(self) -> Data:
        ...

class ExplicitLoopLoader:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def load(self) -> Data:
        _data = {}
        with open(self.file_path) as f:
            for y, line in enumerate(f):
                for x, c in enumerate(line.strip()):
                    _data[(x,y)] = (c == "@")

        return _data

    # GOTCHA: nice "one-liner" using dict comprehension
    def load_gotcha(self) -> Data:
        with open(self.file_path) as f:
            return {
                (x,y): (c == "@")
                for y, line in enumerate(f)
                for x, c in enumerate(line.strip())
            }


class DataImporter:
    def __init__(self, loader: Loader) -> None:
        self.loader = loader

    def import_data(self):
        data = self.loader.load()
        return data

    # TODO: create dataclass fot Data, that will have a print method
    # and other useful methods, e.g. get max_x, max_y, etc.
    @staticmethod 
    def print_data(data: Data) -> None:
        max_x = max(x for x, y in data.keys())
        max_y = max(y for x, y in data.keys())

        for y in range(max_y + 1):
            row = ""
            for x in range(max_x + 1):
                row += "@" if data.get((x,y), False) else "."
            print(row)


class Puzzle:
    def __init__(self, data: Data, solver: Solver) -> None:
        self.data = data
        self.solver = solver

    def run(self) -> int:
        return self.solver.solve(self.data)


def count_adjacent_positions(data: Data, position: Tuple[int,int]) -> int: 
    x, y = position
    adjacent_positions = [
        (x-1, y-1), (x, y-1), (x+1, y-1),
        (x-1, y),             (x+1, y),
        (x-1, y+1), (x, y+1), (x+1, y+1),
    ]

    count = 0
    for pos in adjacent_positions:
        if data.get(pos, False):
            count += 1

    return count

# --- PART 2 ---
# GOTCHA: need to use deepcopy of data to avoid modifying original data
import copy

class AdjacentSolverPart2:
    def solve(self, data: Data) -> int:
        total_count = 0
        count = -1
        data_next = copy.deepcopy(data)
        # GOTCHA: iterating over data.keys() to get positions
        # silly me was iterating in double for loop over x and y

        while count != 0:
            count = 0

            for position in data.keys():
                if data[position]:
                    if count_adjacent_positions(data, position) < 4:
                        count += 1
                        data_next[position] = False

            total_count += count
            data = data_next

        return total_count


def main():
    # file_path = "../puzzle_input/004_test.txt"
    file_path = "../puzzle_input/004.txt"
    loader = ExplicitLoopLoader(file_path=file_path)
    importer = DataImporter(loader=loader)
    data = importer.import_data()

    importer.print_data(data)
    pass

    puzzle = Puzzle(data=data, solver=AdjacentSolverPart2())
    solution = puzzle.run()
    print(f"Total adjacent positions: {solution}")

    
if __name__ == '__main__':
    main()