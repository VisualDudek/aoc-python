from typing import Dict, Protocol, List, Tuple

type Data = Tuple[List[Tuple[int,int]], List[int]]

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


def is_in_range(ranges, id) -> bool:
    for start, end in ranges:
        if start <= id <= end:
            return True
        
    return False


class FreshSolver:
    @staticmethod
    def solve(data: Data) -> int:
        ranges, ids = data
        count = 0

        for id in ids:
            if is_in_range(ranges, id):
                count += 1
        
        return count


def main():
    # file_path = "../puzzle_input/005_test.txt"
    file_path = "../puzzle_input/005.txt"
    loader = ExplicitLoopLoader(file_path=file_path)
    importer = DataImporter(loader=loader)
    data = importer.import_data()

    pass

    puzzle = Puzzle(data=data, solver=FreshSolver())
    solution = puzzle.run()
    print(f"Total adjacent positions: {solution}")

    
if __name__ == '__main__':
    main()