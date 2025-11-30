"""
Python-Specific Techniques Exercises
Based on techniques used in Advent of Code solutions
"""

# ============================================================================
# COLLECTIONS MODULE EXERCISES
# ============================================================================

def exercise_counter_1():
    """
    Exercise: Word Frequency Counter

    Given a list of words, return a dictionary with each word and its count.
    Use Counter from collections module.

    Example:
        Input: ["apple", "banana", "apple", "cherry", "banana", "apple"]
        Output: {"apple": 3, "banana": 2, "cherry": 1}
    """
    # TODO: Implement using Counter
    pass


def exercise_counter_2():
    """
    Exercise: Find Most Common Elements

    Given a list of numbers, find the 3 most common numbers and their counts.
    Use Counter's most_common() method.

    Example:
        Input: [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
        Output: [(4, 4), (3, 3), (2, 2)]
    """
    # TODO: Implement using Counter.most_common()
    pass


def exercise_counter_3():
    """
    Exercise: Character Frequency Match

    Given two strings, determine if they have the same character frequencies.
    Use Counter to compare.

    Example:
        Input: "listen", "silent"
        Output: True (both have same character counts)
    """
    # TODO: Implement using Counter comparison
    pass


def exercise_defaultdict_1():
    """
    Exercise: Group by First Letter

    Given a list of words, group them by their first letter.
    Use defaultdict(list) to avoid key checking.

    Example:
        Input: ["apple", "apricot", "banana", "blueberry", "cherry"]
        Output: {"a": ["apple", "apricot"], "b": ["banana", "blueberry"], "c": ["cherry"]}
    """
    # TODO: Implement using defaultdict(list)
    pass


def exercise_defaultdict_2():
    """
    Exercise: Build Adjacency List

    Given a list of edges (tuples), build a graph adjacency list.
    Use defaultdict(list) for automatic list initialization.

    Example:
        Input: [(1, 2), (1, 3), (2, 4), (3, 4)]
        Output: {1: [2, 3], 2: [4], 3: [4]}
    """
    # TODO: Implement using defaultdict(list)
    pass


def exercise_defaultdict_3():
    """
    Exercise: Running Sum by Category

    Given transactions as (category, amount) tuples, calculate total per category.
    Use defaultdict(int) to avoid initialization.

    Example:
        Input: [("food", 50), ("transport", 20), ("food", 30), ("entertainment", 40)]
        Output: {"food": 80, "transport": 20, "entertainment": 40}
    """
    # TODO: Implement using defaultdict(int)
    pass


# ============================================================================
# DICTIONARY METHODS EXERCISES
# ============================================================================

def exercise_dict_get_1():
    """
    Exercise: Safe Configuration Lookup

    Given a config dictionary and a list of keys, return their values.
    Use dict.get() with default value "NOT_SET" for missing keys.

    Example:
        config = {"host": "localhost", "port": 8080}
        keys = ["host", "port", "timeout"]
        Output: ["localhost", 8080, "NOT_SET"]
    """
    # TODO: Implement using dict.get()
    pass


def exercise_dict_get_2():
    """
    Exercise: Score Calculator with Defaults

    Given a dictionary of scores and a list of students, calculate total.
    Use dict.get() to give 0 points for students not in the dictionary.

    Example:
        scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
        students = ["Alice", "Bob", "David"]
        Output: 177 (85 + 92 + 0)
    """
    # TODO: Implement using dict.get()
    pass


def exercise_dict_get_3():
    """
    Exercise: Merge Dictionaries with Priorities

    Given two dictionaries (primary and fallback), create a merged dictionary.
    For a list of keys, use primary value if exists, otherwise use fallback.

    Example:
        primary = {"a": 1, "b": 2}
        fallback = {"b": 20, "c": 30}
        keys = ["a", "b", "c", "d"]
        Output: {"a": 1, "b": 2, "c": 30, "d": None}
    """
    # TODO: Implement using dict.get()
    pass


def exercise_dict_setdefault():
    """
    Exercise: Count Items Without Counter

    Build a frequency counter manually using dict.setdefault().

    Example:
        Input: ["a", "b", "a", "c", "b", "a"]
        Output: {"a": 3, "b": 2, "c": 1}
    """
    # TODO: Implement using dict.setdefault()
    pass


# ============================================================================
# DATA PROCESSING EXERCISES
# ============================================================================

def exercise_tuple_unpacking_1():
    """
    Exercise: Parse Coordinate Pairs

    Given a list of (x, y) tuples, calculate the sum of all x and y values separately.
    Use tuple unpacking in a loop.

    Example:
        Input: [(1, 2), (3, 4), (5, 6)]
        Output: (9, 12)  # sum of x's = 9, sum of y's = 12
    """
    # TODO: Implement using tuple unpacking
    pass


def exercise_tuple_unpacking_2():
    """
    Exercise: First and Rest Pattern

    Given a list, separate the first element from the rest using unpacking.
    Return them as a tuple.

    Example:
        Input: [10, 20, 30, 40]
        Output: (10, [20, 30, 40])
    """
    # TODO: Implement using extended unpacking (first, *rest)
    pass


def exercise_tuple_unpacking_3():
    """
    Exercise: Swap Values in Dictionary

    Given a dictionary, create a new dictionary with keys and values swapped.
    Use tuple unpacking in dict.items() iteration.

    Example:
        Input: {"name": "Alice", "age": "30"}
        Output: {"Alice": "name", "30": "age"}
    """
    # TODO: Implement using tuple unpacking with .items()
    pass


def exercise_multiple_assignment():
    """
    Exercise: Parse CSV-like Data

    Given strings in format "name,age,city", parse into separate variables.
    Use multiple assignment with str.split().

    Example:
        Input: "Alice,30,NYC"
        Output: name="Alice", age="30", city="NYC"
    """
    # TODO: Implement using multiple assignment
    pass


# ============================================================================
# DESIGN PATTERNS EXERCISES
# ============================================================================

def exercise_callable_1():
    """
    Exercise: Custom Sorter

    Create a function that takes a list and a Callable sorting key function.
    The key function should extract the value to sort by.

    Example:
        Input: [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
        Key function: lambda x: x[1]  (sort by age)
        Output: [("Bob", 25), ("Alice", 30), ("Charlie", 35)]
    """
    # TODO: Implement function accepting Callable parameter
    pass


def exercise_callable_2():
    """
    Exercise: Data Transformer Pipeline

    Create a function that applies a list of transformation functions to data.
    Each transformation is a Callable that takes and returns data.

    Example:
        Input: 5
        Transformations: [lambda x: x * 2, lambda x: x + 10, lambda x: x ** 2]
        Output: 400  # ((5 * 2) + 10) ** 2 = 20 ** 2 = 400
    """
    # TODO: Implement pipeline with Callable list
    pass


def exercise_callable_3():
    """
    Exercise: Strategy Pattern for Scoring

    Implement a score calculator that accepts different scoring strategies.
    Create at least 2 different Callable scoring functions.

    Example scoring strategies:
        - simple_score: sum of all values
        - weighted_score: values multiplied by position (index + 1)

    Example:
        Input: [10, 20, 30]
        simple_score: 60
        weighted_score: 10*1 + 20*2 + 30*3 = 140
    """
    # TODO: Implement with multiple Callable strategies
    pass


# ============================================================================
# BONUS: COMBINED TECHNIQUES
# ============================================================================

def exercise_combined_1():
    """
    Exercise: Word Score Calculator (AoC Style)

    Given a list of words and a letter frequency dictionary, calculate scores.
    Score = sum of (letter count in word * letter frequency in dictionary)
    Use: Counter, dict.get(), tuple unpacking

    Example:
        words = ["hello", "world"]
        frequencies = {"h": 2, "e": 3, "l": 4, "o": 5, "w": 1, "r": 2, "d": 3}

        "hello": h(1*2) + e(1*3) + l(2*4) + o(1*5) = 2+3+8+5 = 18
        "world": w(1*1) + o(1*5) + r(1*2) + l(1*4) + d(1*3) = 1+5+2+4+3 = 15
    """
    # TODO: Combine Counter, dict.get(), and tuple unpacking
    pass


def exercise_combined_2():
    """
    Exercise: Build Graph and Find Paths

    Given edges and a scoring function, build a graph and calculate total score.
    Use: defaultdict, Callable, tuple unpacking

    Example:
        edges = [(1, 2, 10), (1, 3, 20), (2, 3, 15)]  # (from, to, weight)
        score_fn = sum of all weights from node 1
    """
    # TODO: Combine defaultdict, Callable, and tuple unpacking
    pass


# ============================================================================
# SOLUTION TEMPLATES (Uncomment to see solutions)
# ============================================================================

"""
from collections import Counter, defaultdict
from typing import Callable, List, Tuple, Dict, Any

# Solution for exercise_counter_1
def solution_counter_1(words: List[str]) -> Dict[str, int]:
    return dict(Counter(words))

# Solution for exercise_defaultdict_1
def solution_defaultdict_1(words: List[str]) -> Dict[str, List[str]]:
    result = defaultdict(list)
    for word in words:
        result[word[0]].append(word)
    return dict(result)

# Solution for exercise_dict_get_2
def solution_dict_get_2(scores: Dict[str, int], students: List[str]) -> int:
    return sum(scores.get(student, 0) for student in students)

# Solution for exercise_tuple_unpacking_1
def solution_tuple_unpacking_1(coords: List[Tuple[int, int]]) -> Tuple[int, int]:
    sum_x, sum_y = 0, 0
    for x, y in coords:
        sum_x += x
        sum_y += y
    return sum_x, sum_y

# Solution for exercise_callable_2
def solution_callable_2(data: Any, transformations: List[Callable]) -> Any:
    result = data
    for transform in transformations:
        result = transform(result)
    return result
"""


if __name__ == "__main__":
    print("Python Techniques Exercises")
    print("=" * 50)
    print("\nComplete each exercise by implementing the TODO sections.")
    print("Run tests to verify your solutions.\n")
    print("Exercise categories:")
    print("  1. Collections Module (Counter, defaultdict)")
    print("  2. Dictionary Methods (get, setdefault)")
    print("  3. Data Processing (tuple unpacking, multiple assignment)")
    print("  4. Design Patterns (Callable, strategy pattern)")
    print("  5. Combined Techniques (real AoC-style problems)")
