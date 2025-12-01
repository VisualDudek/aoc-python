from typing import Protocol, Tuple, List


type Data = List[Tuple[str, int]]

class Loader(Protocol):
    def load(self) -> Data:
        ...

class Solver(Protocol):
    def solve(self, data: Data) -> int:
        ...

class SplitOnFirst:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def load(self) -> Data:
        data = []
        with open(self.file_path) as f:
            for line in f:
                first, rest = line[:1], line[1:]
                data.append((first, int(rest)))

        return data
    
class BruteForceSolverPart2:
    def solve(self, data: Data) -> int:
        dial = 50
        total_zeros = 0

        # Bute force simulation
        for c, i in data:
            for _step in range(i):
                if c == "R":
                    dial += 1
                else:
                    dial -= 1

                dial = dial % 100

                if dial == 0:
                    total_zeros += 1

        return total_zeros

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
        
    

def main():
    file_path = "puzzle_input/001.txt"
    loader = SplitOnFirst(file_path=file_path)
    importer = DataImporter(loader=loader)
    data = importer.import_data()

    solver = BruteForceSolverPart2()
    puzzle = Puzzle(data=data, solver=solver)
    solution = puzzle.run()
    assert solution == 6634
    print(f"Total dial points at 0 is: {solution}")


if __name__ == "__main__":
    main()