from typing import Protocol, List, Tuple
import numpy as np
from utils import DataImporter, Loader

type Data = List[str]

class ExplicitLoopLoader:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def load(self) -> Data:
        data_list = []
        with open(self.file_path) as f:
            for line in f:
                data_list.append(line.strip())

        return data_list

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
    loader = ExplicitLoopLoader(file_path=file_path)
    importer = DataImporter(loader=loader)
    data = importer.import_data()
    pass
    

if __name__ == "__main__":
    main()