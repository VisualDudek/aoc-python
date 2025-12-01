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

class DataProcessor:
    def __init__(self, data: Data) -> None:
        self.data = data

    def process(self) -> int:
        dial = 50
        total_zeros = 0

        # Bute force simulation
        for c, i in self.data:
            for _step in range(i):
                if c == "R":
                    dial += 1
                else:
                    dial -= 1

                dial = dial % 100

                if dial == 0:
                    total_zeros += 1

        return total_zeros
    

def main():
    file_path = "puzzle_input/001.txt"
    loader = SplitOnFirst(file_path=file_path)
    importer = DataImporter(loader=loader)
    data = importer.import_data()

    data_processor = DataProcessor(data)
    solution = data_processor.process()
    assert solution == 6634
    print(f"Total dial points at 0 is: {solution}")


if __name__ == "__main__":
    main()