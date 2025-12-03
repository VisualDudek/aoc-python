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
        for line_no, jolt in enumerate(data):
            print(f"Processing line number: {line_no}")
            max_jolt = find_max_jolt(jolt)
            len_max_jolt = len(str(max_jolt))
            _total_sum += max_jolt

        return _total_sum 


# --- PART 2 ---
from itertools import combinations
def find_max_jolt_brute_force(numbers: str) -> int:
    # Brute Force FAILS

    _res_tmp = []
    combos = [int(''.join(c)) for c in combinations(numbers, 12)]

    return max(combos)


def find_max_jolt_draft(numbers: str) -> int:
    # Draft solution NOT COMPLETED
    _int_list = [int(s) for s in numbers]

    _end_idx = len(numbers)

    first = max(_int_list[0:_end_idx - 12])
    first_idx = numbers.find(str(first))

    second = max(_int_list[first_idx+1:_end_idx - 11])

    res = first*10**11 + second*10**10

    return res


def find_max_jolt(numbers: str) -> int:
    _int_list = [int(s) for s in numbers]

    _end_idx = len(numbers)
    _res_tmp = []
    _start_idx = 0

    for i in range(12,0,-1):
        first = max(_int_list[_start_idx:_end_idx - i + 1])
        first_idx = numbers.find(str(first), _start_idx)
        _start_idx = first_idx + 1

        _res_tmp.append(first)
    
    return int(''.join(map(str, _res_tmp)))
    
    


def main():
    # file_path = "puzzle_input/003_test.txt"
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