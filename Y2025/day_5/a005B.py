from typing import Dict, Protocol, List, Tuple

type Data = Tuple[List[Tuple[int,int]], List[int]]

class Solver(Protocol):
    @staticmethod
    def solve(data: Data) -> int:
        ...

class Loader(Protocol):
    def load(self) -> Data:
        ...

class ExplicitLoopLoader:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def load(self) -> Data:
        _ranges = []
        _data = []

        is_first_part = True

        with open(self.file_path) as f:
            for line in f:
                if line.strip() == "":
                    is_first_part = False
                    continue    

                if is_first_part:
                    start, end = line.strip().split("-")
                    _ranges.append((int(start), int(end)))

                else:
                    _id = line.strip()
                    _data.append(int(_id))

        return _ranges, _data


class DataImporter:
    def __init__(self, loader: Loader) -> None:
        self.loader = loader

    def import_data(self):
        data = self.loader.load()
        return data


class Puzzle:
    def __init__(self, data: Data, solver: Solver) -> None:
        self.data = data
        self.solver = solver

    def run(self) -> int:
        return self.solver.solve(self.data)


def is_in_range(range, id) -> bool:
    start, end = range
    if start <= id <= end:
        return True
        
    return False


def sum_ranges(ranges) -> int:
    total = 0
    for start, end in ranges:
        total += end - start + 1
    return total


class FreshSolverPart2:
    @staticmethod
    def solve(data: Data):
        ranges, ids = data

        ranges_merged = [(0,0)] # dummy range to simplify logic

        ranges = sorted(ranges, key=lambda x: x[0])

        for current_start, current_end in ranges:
            last_tuple = ranges_merged[-1]
            last_start, last_end = ranges_merged[-1]

            if is_in_range(last_tuple, current_start) or is_in_range(last_tuple, current_end):
                # modify last 
                ranges_merged[-1] = (min(last_start,current_start)), max(last_end, current_end)
            else:
                # add new range
                ranges_merged.append((current_start, current_end))

        return sum_ranges(ranges_merged[1:])  # exclude dummy range


def main():
    # file_path = "../puzzle_input/005_test.txt"
    file_path = "../puzzle_input/005.txt"
    loader = ExplicitLoopLoader(file_path=file_path)
    importer = DataImporter(loader=loader)
    data = importer.import_data()

    pass

    # GOTCHA:
    # check if overlap
    # if yes take min(bgn) max(end)
    # to avoid multiple overlapping ranges in the end first sort ranges
    # with key on bgn

    puzzle = Puzzle(data=data, solver=FreshSolverPart2())
    solution = puzzle.run()
    print(f"Total fresh ingredients: {solution}")

    
if __name__ == '__main__':
    main()