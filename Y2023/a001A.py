from typing import Protocol, List, Tuple
import numpy as np
from utils import DataImporter, Loader

type Data = List[int]

class Solver(Protocol):
    def solve(self, data: Data) -> int:
        ...

class ExplicitLoopLoader:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def load(self) -> Data:
        data_list = []
        with open(self.file_path) as f:
            for line in f:
                _tmp = []
                for c in line:
                    if c.isdigit():
                        _tmp.append(c)

                first, last = _tmp[0], _tmp[-1]
                data_list.append(int(first + last))

        return data_list


class Puzzle:
    def __init__(self, data: Data, solver: Solver) -> None:
        self.data = data
        self.solver = solver

    def run(self) -> int:
        return self.solver.solve(self.data)
    

class SumSolver:
    def solve(self, data: Data) -> int:
        return sum(data)
    

def main():
    file_path = "puzzle_input/001.txt"
    loader = ExplicitLoopLoader(file_path=file_path)
    importer = DataImporter(loader=loader)
    data = importer.import_data()

    puzzle = Puzzle(data=data, solver=SumSolver())
    result = puzzle.run()
    print(result)
    

if __name__ == "__main__":
    main()