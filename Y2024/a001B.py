from typing import List, Protocol, Callable
import utils
from collections import defaultdict, Counter

class DataImporter:
    def __init__(self, loader: utils.Loader) -> None:
        self.loader = loader

    def import_data(self):
        data = self.loader.load()
        return data


class PuzzleSolution:
    def __init__(
            self, data: utils.Data,
            solution: Callable[[utils.Data], int]) -> None:
        self.data = data
        self.solution = solution

    def run(self) -> int:
        return self.solution(self.data)
    

def similarity_score(data: utils.Data) -> int:
    left, right = data
    right_counter = Counter(right)
    score = 0
    for l in left:
        if l in right_counter:
            score += l * right_counter[l]
    return score


def similarity_score_defaultdict(data: utils.Data) -> int:
    left, right = data
    right_dict = defaultdict(int)

    for r in right:
        right_dict[r] += 1

    score = 0
    for l in left:
        if l in right_dict:
            score += l * right_dict[l]
    return score


def similarity_score_dict(data: utils.Data) -> int:
    left, right = data
    right_dict = {}

    for r in right:
        right_dict[r] = right_dict.get(r, 0) + 1

    score = 0
    for l in left:
        score += l * right_dict.get(l, 0)

    return score


def main():
    file_path = "puzzle_input/001.txt"
    loader = utils.NumpyLoader(file_path=file_path)
    importer = DataImporter(loader=loader)
    data = importer.import_data()

    puzzle_solution = PuzzleSolution(
        data=data,
        # solution=similarity_score,
        # solution=similarity_score_defaultdict,
        solution=similarity_score_dict,
    )
    result = puzzle_solution.run()
    assert result == 20373490
    print(f"Similarity score: {result}")

if __name__ == "__main__":
    main()