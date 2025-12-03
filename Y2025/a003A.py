from typing import Protocol, List, Tuple

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
        _data_list = []
        with open(self.file_path) as f:
            lines = f.read().strip().split()
            for line in lines:
                _data_list.append(line)

        return _data_list


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
    

class PuzzleSolver:
    @staticmethod
    def solve(data: Data):
        _total_sum = 0
        for jolt in data:
            max_jolt = find_max_jolt(jolt)
            _total_sum += max_jolt

        return _total_sum 


def find_max_jolt(numbers: str) -> int:
    numbers_int = [int(s) for s in numbers]

    _res_tmp = []
    end_idx = len(numbers)

    for i in range(1,end_idx):
        left = max(numbers_int[0:i])
        right = max(numbers_int[i:end_idx])

        _res_tmp.append(left*10 + right)

    return max(_res_tmp)    

def main():
    file_path = "puzzle_input/003.txt"
    loader = ExplicitLoopLoader(file_path=file_path)
    importer = DataImporter(loader=loader)
    data = importer.import_data()
    pass

    puzzle = Puzzle(data=data, solver=PuzzleSolver())
    solution = puzzle.run()
    # assert solution == 18700015741
    print(f"Max jolt sum: {solution}")
    

if __name__ == "__main__":
    main()