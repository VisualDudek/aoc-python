from typing import Callable, Dict, Generator, Protocol, List, Tuple

type Data = List[List[str]]

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
        _data = []

        with open(self.file_path) as f:
            for line in f:
                _data.append(line.strip().split())

        return _data


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


def iterate_over_columns(data: Data) -> Generator[tuple[str]]:

    _res = (col_values for col_values in zip(*data))

    return _res

# GOTCHA: you can use mul and add from operator module
from operator import mul, add
from functools import reduce

class SumSolverPart1:
    @staticmethod
    def solve(data: Data) -> int:
        numbers: List[List[str]] = data[:-1]
        operators: List[str] = data[-1]

        numbers_by_column_gen: List[tuple[str, ...]] = list(iterate_over_columns(numbers))

        total = 0

        OPERATORS: dict[str, Callable[[int, int], int]] = {
            "+": add,
            "*": mul,
        }

        # GOTCHA: you can go here with "folding" functional approach
        # GOTCHA: you can use zip to iterate simultaneously over operators and columns
        # GOTCHA: numbers and number var names are confusing here
        # GOTCHA: you can get rid of total variable with sum and return directly
        for symbol, number in zip(operators, numbers_by_column_gen):
            op = OPERATORS[symbol]
            total += reduce(op, (int(n) for n in number))

        return total


def main():
    # file_path = "../puzzle_input/006_test.txt"
    file_path = "../puzzle_input/006.txt"
    loader = ExplicitLoopLoader(file_path=file_path)
    importer = DataImporter(loader=loader)
    data = importer.import_data()
    pass

    puzzle = Puzzle(data=data, solver=SumSolverPart1())
    solution = puzzle.run()
    # assert solution ==  # Test
    assert solution == 6417439773370 # My Puzzle Input
    print(f"Total sum is: {solution}")

    
if __name__ == '__main__':
    main()