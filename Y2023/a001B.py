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
        data_list = []
        with open(self.file_path) as f:
            for line in f:
                data_list.append(line.strip())

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
    

class SumSolver:
    def solve(self, data: Data) -> int:
        data_list = []
        for line in data:
            _tmp = []
            for c in line:
                if c.isdigit():
                    _tmp.append(c)

            first, last = _tmp[0], _tmp[-1]
            data_list.append(int(first + last))

        return sum(data_list)
    

def data_transformer_wrong(data: Data) -> Data:
    res_data = []
    numbers_dict = {
        'one': '1', 
        'two': '2', 
        'three': '3', 
        'four': '4', 
        'five': '5', 
        'six': '6', 
        'seven': '7', 
        'eight': '8', 
        'nine': '9',
        }
    for line in data:
        for k, v in numbers_dict.items():
            line = line.replace(k, v)
        res_data.append(line)

    return res_data
    

def data_transformer(data: Data) -> Data:
    res_data = []
    numbers_dict = {
        'one': '1', 
        'two': '2', 
        'three': '3', 
        'four': '4', 
        'five': '5', 
        'six': '6', 
        'seven': '7', 
        'eight': '8', 
        'nine': '9',
        }
    for line in data:
        for i in range(len(line)):
            # TODO

    return res_data


def main():
    file_path = "puzzle_input/001_test.txt"
    loader = ExplicitLoopLoader(file_path=file_path)
    importer = DataImporter(loader=loader)
    data = importer.import_data()
    pass

    data = data_transformer(data)
    pass

    puzzle = Puzzle(data=data, solver=SumSolver())
    result = puzzle.run()
    print(result)
    

if __name__ == "__main__":
    main()