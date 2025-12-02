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

# what wnt wrong here?    
# helper fn from Reddit solution
import re

def reddit(line: str) -> int: 
    nums = 'one|two|three|four|five|six|seven|eight|nine'
    nums_re = re.compile(r'(?=(\d|%s))' % nums)
    nums = nums.split('|')

    digits = []
    for num in nums_re.findall(line):
        if num in nums:
            num = str(nums.index(num) + 1)
        digits.append(num)
    total = int(digits[0] + digits[-1])

    return total


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
    data_res = []
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
    FIRST_LETTERS = ('o', 't', 'f', 's', 'e')
    for line in data:
        i = 0
        line_tmp = ''
        while i < len(line):
            if i+3 <= len(line) and line[i:i+3] in ('one', 'two', 'six'):
                line_tmp += numbers_dict[line[i:i+3]]
                # i += 3
            elif i+4 <= len(line) and line[i:i+4] in ('four', 'five', 'nine'):
                line_tmp += numbers_dict[line[i:i+4]]
                # i += 4
            elif i+5 <= len(line) and line[i:i+5] in ('three', 'seven', 'eight'):
                line_tmp += numbers_dict[line[i:i+5]]
                # i += 5
            else:
                line_tmp += line[i]
                # i += 1
            i += 1

        data_res.append(line_tmp)
        print(f"Transformed line: {line} -> {line_tmp}")

        # checking what went wrong
        # cSpell:disable-next-line
        # FOUND IT: 28gtbkszmrtmnineoneightmx -> 28gtbkszmrtm91ightmx 
        # missing last 9 because of faulty replacement logic with overlapping patterns
        # incrementing i by one solved it, enabling overlapping pattern checks
        _tmp = []
        for c in line_tmp:
            if c.isdigit():
                _tmp.append(c)

        first, last = _tmp[0], _tmp[-1]

        assert reddit(line) == int(first + last)

    return data_res


def main():
    file_path = "puzzle_input/001.txt"
    loader = ExplicitLoopLoader(file_path=file_path)
    importer = DataImporter(loader=loader)
    data = importer.import_data()
    pass

    data_post = data_transformer(data)
    pass

    puzzle = Puzzle(data=data_post, solver=SumSolver())
    result = puzzle.run()
    assert result == 54265
    print(result)
    

if __name__ == "__main__":
    main()