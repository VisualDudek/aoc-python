from typing import Dict, Generator, Protocol, List, Tuple

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


def iterate_over_columns(data: Data) -> Generator[List[str]]:

    _res = (col_values for col_values in zip(*data))

    return _res


class SumSolverPart1:
    @staticmethod
    def solve(data: Data) -> int:
        numbers = data[:-1]
        operators = data[-1]

        numbers_by_column_gen = iterate_over_columns(numbers)

        total = 0

        for operator in operators:
            if operator == "+":
                total += sum(int(n) for n in next(numbers_by_column_gen))
            elif operator == "*":
                prod = 1
                for n in next(numbers_by_column_gen):
                    prod *= int(n)
                total += prod

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
    print(f"Total sum is: {solution}")

    
if __name__ == '__main__':
    main()