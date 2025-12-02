from typing import Protocol, List, Tuple
from textwrap import wrap
from utils import timed

type Data = List[Tuple[str, str]]

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
        data_list = []
        with open(self.file_path) as f:
            line = f.read().strip()
            ranges = line.split(",")
            for r in ranges:
                start, end = r.split("-")
                data_list.append((start, end))

        return data_list


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

    @timed
    def run(self) -> int:
        return self.solver.solve(self.data)
    
from functools import lru_cache

@lru_cache(maxsize=None)
def is_valid_id(number: str) -> bool:

    upper = len(number) // 2

    for n in range(1, upper + 1):
        s = wrap(number, n)

        if len(set(s)) == 1:
            return False

    return True


def is_valid_id_factors(number: str) -> bool:

    FACTORS = {1: [], 2: [1], 3: [1], 4: [2, 1], 5: [1], 6: [3, 2, 1], 7: [1], 8: [4, 2, 1], 9: [3, 1], 10: [5, 2, 1]}

    for n in FACTORS[len(number)]:
        s = wrap(number, n)

        if len(set(s)) == 1:
            return False

    return True

def is_valid_id_custom_wrap(number: str) -> bool:

    FACTORS = {1: [], 2: [1], 3: [1], 4: [2, 1], 5: [1], 6: [3, 2, 1], 7: [1], 8: [4, 2, 1], 9: [3, 1], 10: [5, 2, 1]}

    for n in FACTORS[len(number)]:

        if len(set(str(number)[j:j + n] for j in range(0, len(number), n))) == 1:
            return False

    return True

class PuzzleSolver:
    def __init__(self, is_valid=is_valid_id) -> None:
        self.is_valid = is_valid

    def solve(self, data: Data) -> int:
        _res: List[int] = []
        for first, last in data:
            for i in range(int(first), int(last)+ 1):
                if not self.is_valid(str(i)):
                    _res.append(i)

        return sum(_res)


def main():
    file_path = "puzzle_input/002.txt"
    loader = ExplicitLoopLoader(file_path=file_path)
    importer = DataImporter(loader=loader)
    data = importer.import_data()
    pass

    solver = PuzzleSolver(is_valid=is_valid_id_custom_wrap) 
    puzzle = Puzzle(data=data, solver=solver)
    solution = puzzle.run()
    assert solution == 20077272987
    print(f"Sum of invalid IDs: {solution}")

    # print(f"Cache info: {is_valid_id.cache_info()}")

if __name__ == "__main__":
    main()