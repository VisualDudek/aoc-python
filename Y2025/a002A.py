from typing import Protocol, List, Tuple

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

    def run(self) -> int:
        return self.solver.solve(self.data)
    

def is_valid_id(number: str) -> bool:

    if len(number) % 2 == 1:
        return True
    
    half_idx = int(len(number) / 2)
 
    return number[:half_idx] != number[half_idx:]


class PuzzleSolver:
    def solve(self, data: Data):
        _res: List[int] = []
        for first, last in data:
            for i in range(int(first), int(last)+ 1):
                if not is_valid_id(str(i)):
                    _res.append(i)

        return sum(_res)


def main():
    file_path = "puzzle_input/002.txt"
    loader = ExplicitLoopLoader(file_path=file_path)
    importer = DataImporter(loader=loader)
    data = importer.import_data()
    pass

    puzzle = Puzzle(data=data, solver=PuzzleSolver())
    solution = puzzle.run()
    assert solution == 18700015741
    print(f"Sum of invalid IDs: {solution}")
    

if __name__ == "__main__":
    main()