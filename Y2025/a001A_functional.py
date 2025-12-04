from typing import Protocol, Tuple, List


type Data = List[Tuple[str, int]]

class Loader(Protocol):
    def load(self) -> Data:
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

class DataImporter:
    def __init__(self, loader: Loader) -> None:
        self.loader = loader

    def import_data(self):
        data = self.loader.load()
        return data


def process(c:str, i:int):
    dial = 50 # closure initial value

    def f(c:str, i:int) -> int:
        nonlocal dial
        if c == "R":
            dial += i
            dial = dial % 100
        else:
            dial -= i
            dial = dial % 100

        if dial == 0:
            return 1
        return 0
    return f(c, i)
    

def main():
    file_path = "puzzle_input/001.txt"
    loader = SplitOnFirst(file_path=file_path)
    importer = DataImporter(loader=loader)
    data = importer.import_data()

    dial = 50
    solution = sum(map(lambda x: process(*x), data))

    print(f"Total dial points at 0 is: {solution}")


if __name__ == "__main__":
    main()