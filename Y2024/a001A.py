from typing import Protocol, List, Tuple
import numpy as np


type Data = Tuple[List[int], List[int]]

class Loader(Protocol):
    def load(self) -> Data:
        ...

class ZipLoader:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def load(self) -> Data:
        with open(self.file_path) as f:
            left, right = zip(*[line.split() for line in f])
            left = list(map(int, left))
            right = list(map(int, right))

        return left, right
    

class ExplicitLoopLoader:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def load(self) -> Data:
        left, right = [], []
        with open(self.file_path) as f:
            for line in f:
                l, r = line.split()
                left.append(int(l))
                right.append(int(r))

        return left, right
    

class NumpyLoader:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def load(self) -> Data:
        data = np.loadtxt(self.file_path, dtype=int) # cSpell:ignore loadtxt
        left = data[:, 0].tolist()
        right = data[:, 1].tolist()
        return left, right


class DataImporter:
    def __init__(self, loader: Loader) -> None:
        self.loader = loader

    def import_data(self):
        data = self.loader.load()
        return data

class DataProcessor:
    def __init__(self, data: Data) -> None:
        self.left, self.right = data

    def process(self) -> int:
        self.left.sort()
        self.right.sort()
        distances: List[int] = [abs(l - r) for l, r in zip(self.left, self.right)]
        return sum(distances)
    

def main():
    file_path = "puzzle_input/001.txt"
    loader = NumpyLoader(file_path=file_path)
    importer = DataImporter(loader=loader)
    data = importer.import_data()
    
    processor = DataProcessor(data=data)
    result = processor.process()
    print(f"Total distance: {result}")


if __name__ == "__main__":
    main()