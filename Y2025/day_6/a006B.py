from typing import Dict, Generator, Protocol, List, Tuple

type Data = List[str]

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

        with open(self.file_path) as f:
            _lines = f.read().splitlines()

        return _lines


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


def columns_generator(data: Data) -> Generator[tuple[str]]:

    _res = (col_values for col_values in zip(*data))

    return _res

import re
def get_pos_of_operators(operators: str) -> List[int]:
    _col_positions = [m.start() for m in re.finditer(r'[+*]', operators)]

    # add end position for last column
    _col_positions.append(len(operators) + 1)

    return _col_positions


def pairs_of_col_positions(col_positions: List[int]) -> List[Tuple[int,int]]:
    _res = []

    # TODO: try with `zip`
    for i in range(len(col_positions) - 1):
        _res.append((col_positions[i], col_positions[i+1]-1))

    return _res

def parse_lines_by_ranges(lines: List[str], col_ranges: List[Tuple[int,int]]) -> List[List[str]]:
    _res = []

    for start, end in col_ranges:
        _col_values = [line[start:end] for line in lines]
        _res.append(_col_values)

    return _res

def transpose_data_in_column(data: List[str]) -> List[int]:
    _res = []

    for col_values in zip(*data):
        _res.append(int("".join(col_values)))

    return _res


# --- Part 2 ---
class SumSolverPart2:
    @staticmethod
    def solve(data: Data) -> int:
        numbers: List[str] = data[:-1]
        operators = data[-1]
        total = 0

        cols_str = parse_lines_by_ranges(numbers, pairs_of_col_positions(get_pos_of_operators(operators)))  

        for operator in operators.split():
            if operator == "+":
                total += sum(transpose_data_in_column(cols_str.pop(0)))
            elif operator == "*":
                prod = 1
                for n in transpose_data_in_column(cols_str.pop(0)):
                    prod *= n
                total += prod

        return total


def main():
    # file_path = "../puzzle_input/006_test.txt"
    file_path = "../puzzle_input/006.txt"
    loader = ExplicitLoopLoader(file_path=file_path)
    importer = DataImporter(loader=loader)
    data = importer.import_data()
    pass

    puzzle = Puzzle(data=data, solver=SumSolverPart2())
    solution = puzzle.run()
    print(f"Total sum is: {solution}")

    
if __name__ == '__main__':
    main()