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
