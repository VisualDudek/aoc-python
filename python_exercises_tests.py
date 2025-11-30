"""
Tests and Solutions for Python Techniques Exercises
Run with: python python_exercises_tests.py
"""

from collections import Counter, defaultdict
from typing import Callable, List, Tuple, Dict, Any


# ============================================================================
# SOLUTIONS - Collections Module
# ============================================================================

def solution_counter_1(words: List[str]) -> Dict[str, int]:
    """Solution using Counter"""
    return dict(Counter(words))


def solution_counter_2(numbers: List[int], n: int = 3) -> List[Tuple[int, int]]:
    """Solution using Counter.most_common()"""
    return Counter(numbers).most_common(n)


def solution_counter_3(str1: str, str2: str) -> bool:
    """Solution using Counter comparison"""
    return Counter(str1) == Counter(str2)


def solution_defaultdict_1(words: List[str]) -> Dict[str, List[str]]:
    """Solution using defaultdict(list)"""
    result = defaultdict(list)
    for word in words:
        result[word[0]].append(word)
    return dict(result)


def solution_defaultdict_2(edges: List[Tuple[int, int]]) -> Dict[int, List[int]]:
    """Solution using defaultdict(list) for adjacency list"""
    graph = defaultdict(list)
    for from_node, to_node in edges:
        graph[from_node].append(to_node)
    return dict(graph)


def solution_defaultdict_3(transactions: List[Tuple[str, int]]) -> Dict[str, int]:
    """Solution using defaultdict(int)"""
    totals = defaultdict(int)
    for category, amount in transactions:
        totals[category] += amount
    return dict(totals)


# ============================================================================
# SOLUTIONS - Dictionary Methods
# ============================================================================

def solution_dict_get_1(config: Dict[str, Any], keys: List[str]) -> List[Any]:
    """Solution using dict.get() with default"""
    return [config.get(key, "NOT_SET") for key in keys]


def solution_dict_get_2(scores: Dict[str, int], students: List[str]) -> int:
    """Solution using dict.get() for safe score calculation"""
    return sum(scores.get(student, 0) for student in students)


def solution_dict_get_3(
    primary: Dict[str, Any],
    fallback: Dict[str, Any],
    keys: List[str]
) -> Dict[str, Any]:
    """Solution using dict.get() for merged lookup"""
    return {key: primary.get(key, fallback.get(key)) for key in keys}


def solution_dict_setdefault(items: List[str]) -> Dict[str, int]:
    """Solution using dict.setdefault()"""
    counts = {}
    for item in items:
        counts[item] = counts.setdefault(item, 0) + 1
    return counts


# ============================================================================
# SOLUTIONS - Data Processing
# ============================================================================

def solution_tuple_unpacking_1(coords: List[Tuple[int, int]]) -> Tuple[int, int]:
    """Solution using tuple unpacking in loop"""
    sum_x, sum_y = 0, 0
    for x, y in coords:
        sum_x += x
        sum_y += y
    return sum_x, sum_y


def solution_tuple_unpacking_2(lst: List[Any]) -> Tuple[Any, List[Any]]:
    """Solution using extended unpacking"""
    first, *rest = lst
    return first, rest


def solution_tuple_unpacking_3(d: Dict[str, str]) -> Dict[str, str]:
    """Solution using tuple unpacking with .items()"""
    return {value: key for key, value in d.items()}


def solution_multiple_assignment(csv_string: str) -> Tuple[str, str, str]:
    """Solution using multiple assignment"""
    name, age, city = csv_string.split(",")
    return name, age, city


# ============================================================================
# SOLUTIONS - Design Patterns
# ============================================================================

def solution_callable_1(
    data: List[Tuple[str, int]],
    key_fn: Callable
) -> List[Tuple[str, int]]:
    """Solution accepting Callable sorting key"""
    return sorted(data, key=key_fn)


def solution_callable_2(data: Any, transformations: List[Callable]) -> Any:
    """Solution implementing transformation pipeline"""
    result = data
    for transform in transformations:
        result = transform(result)
    return result


def solution_callable_3_simple(values: List[int]) -> int:
    """Simple scoring strategy: sum"""
    return sum(values)


def solution_callable_3_weighted(values: List[int]) -> int:
    """Weighted scoring strategy: value * position"""
    return sum(value * (index + 1) for index, value in enumerate(values))


def solution_callable_3_calculator(
    values: List[int],
    strategy: Callable[[List[int]], int]
) -> int:
    """Score calculator accepting strategy"""
    return strategy(values)


# ============================================================================
# SOLUTIONS - Combined Techniques
# ============================================================================

def solution_combined_1(words: List[str], frequencies: Dict[str, int]) -> Dict[str, int]:
    """Solution combining Counter and dict.get()"""
    scores = {}
    for word in words:
        letter_counts = Counter(word)
        score = sum(
            count * frequencies.get(letter, 0)
            for letter, count in letter_counts.items()
        )
        scores[word] = score
    return scores


def solution_combined_2(
    edges: List[Tuple[int, int, int]],
    start_node: int,
    score_fn: Callable[[List[int]], int]
) -> int:
    """Solution combining defaultdict, Callable, and tuple unpacking"""
    graph = defaultdict(list)
    for from_node, to_node, weight in edges:
        graph[from_node].append((to_node, weight))

    # Extract weights from start_node
    weights = [weight for _, weight in graph[start_node]]
    return score_fn(weights)


# ============================================================================
# TESTS
# ============================================================================

def test_counter_exercises():
    print("Testing Counter exercises...")

    # Test 1
    words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    result = solution_counter_1(words)
    assert result == {"apple": 3, "banana": 2, "cherry": 1}, f"Failed: {result}"
    print("  ✓ Counter exercise 1 passed")

    # Test 2
    numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    result = solution_counter_2(numbers, 3)
    assert result == [(4, 4), (3, 3), (2, 2)], f"Failed: {result}"
    print("  ✓ Counter exercise 2 passed")

    # Test 3
    assert solution_counter_3("listen", "silent") == True
    assert solution_counter_3("hello", "world") == False
    print("  ✓ Counter exercise 3 passed")


def test_defaultdict_exercises():
    print("\nTesting defaultdict exercises...")

    # Test 1
    words = ["apple", "apricot", "banana", "blueberry", "cherry"]
    result = solution_defaultdict_1(words)
    expected = {"a": ["apple", "apricot"], "b": ["banana", "blueberry"], "c": ["cherry"]}
    assert result == expected, f"Failed: {result}"
    print("  ✓ defaultdict exercise 1 passed")

    # Test 2
    edges = [(1, 2), (1, 3), (2, 4), (3, 4)]
    result = solution_defaultdict_2(edges)
    assert result == {1: [2, 3], 2: [4], 3: [4]}, f"Failed: {result}"
    print("  ✓ defaultdict exercise 2 passed")

    # Test 3
    transactions = [("food", 50), ("transport", 20), ("food", 30), ("entertainment", 40)]
    result = solution_defaultdict_3(transactions)
    assert result == {"food": 80, "transport": 20, "entertainment": 40}, f"Failed: {result}"
    print("  ✓ defaultdict exercise 3 passed")


def test_dict_get_exercises():
    print("\nTesting dict.get() exercises...")

    # Test 1
    config = {"host": "localhost", "port": 8080}
    keys = ["host", "port", "timeout"]
    result = solution_dict_get_1(config, keys)
    assert result == ["localhost", 8080, "NOT_SET"], f"Failed: {result}"
    print("  ✓ dict.get() exercise 1 passed")

    # Test 2
    scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
    students = ["Alice", "Bob", "David"]
    result = solution_dict_get_2(scores, students)
    assert result == 177, f"Failed: {result}"
    print("  ✓ dict.get() exercise 2 passed")

    # Test 3
    primary = {"a": 1, "b": 2}
    fallback = {"b": 20, "c": 30}
    keys = ["a", "b", "c", "d"]
    result = solution_dict_get_3(primary, fallback, keys)
    assert result == {"a": 1, "b": 2, "c": 30, "d": None}, f"Failed: {result}"
    print("  ✓ dict.get() exercise 3 passed")

    # Test setdefault
    items = ["a", "b", "a", "c", "b", "a"]
    result = solution_dict_setdefault(items)
    assert result == {"a": 3, "b": 2, "c": 1}, f"Failed: {result}"
    print("  ✓ dict.setdefault() exercise passed")


def test_tuple_unpacking_exercises():
    print("\nTesting tuple unpacking exercises...")

    # Test 1
    coords = [(1, 2), (3, 4), (5, 6)]
    result = solution_tuple_unpacking_1(coords)
    assert result == (9, 12), f"Failed: {result}"
    print("  ✓ Tuple unpacking exercise 1 passed")

    # Test 2
    lst = [10, 20, 30, 40]
    result = solution_tuple_unpacking_2(lst)
    assert result == (10, [20, 30, 40]), f"Failed: {result}"
    print("  ✓ Tuple unpacking exercise 2 passed")

    # Test 3
    d = {"name": "Alice", "age": "30"}
    result = solution_tuple_unpacking_3(d)
    assert result == {"Alice": "name", "30": "age"}, f"Failed: {result}"
    print("  ✓ Tuple unpacking exercise 3 passed")

    # Test multiple assignment
    csv_string = "Alice,30,NYC"
    result = solution_multiple_assignment(csv_string)
    assert result == ("Alice", "30", "NYC"), f"Failed: {result}"
    print("  ✓ Multiple assignment exercise passed")


def test_callable_exercises():
    print("\nTesting Callable exercises...")

    # Test 1
    data = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
    result = solution_callable_1(data, key_fn=lambda x: x[1])
    assert result == [("Bob", 25), ("Alice", 30), ("Charlie", 35)], f"Failed: {result}"
    print("  ✓ Callable exercise 1 passed")

    # Test 2
    transformations = [lambda x: x * 2, lambda x: x + 10, lambda x: x ** 2]
    result = solution_callable_2(5, transformations)
    assert result == 400, f"Failed: {result}"
    print("  ✓ Callable exercise 2 passed")

    # Test 3
    values = [10, 20, 30]
    assert solution_callable_3_calculator(values, solution_callable_3_simple) == 60
    assert solution_callable_3_calculator(values, solution_callable_3_weighted) == 140
    print("  ✓ Callable exercise 3 passed")


def test_combined_exercises():
    print("\nTesting combined technique exercises...")

    # Test 1
    words = ["hello", "world"]
    frequencies = {"h": 2, "e": 3, "l": 4, "o": 5, "w": 1, "r": 2, "d": 3}
    result = solution_combined_1(words, frequencies)
    assert result == {"hello": 18, "world": 15}, f"Failed: {result}"
    print("  ✓ Combined exercise 1 passed")

    # Test 2
    edges = [(1, 2, 10), (1, 3, 20), (2, 3, 15)]
    result = solution_combined_2(edges, 1, sum)
    assert result == 30, f"Failed: {result}"
    print("  ✓ Combined exercise 2 passed")


def run_all_tests():
    print("=" * 60)
    print("Running Python Techniques Exercise Tests")
    print("=" * 60)

    test_counter_exercises()
    test_defaultdict_exercises()
    test_dict_get_exercises()
    test_tuple_unpacking_exercises()
    test_callable_exercises()
    test_combined_exercises()

    print("\n" + "=" * 60)
    print("✓ All tests passed!")
    print("=" * 60)


if __name__ == "__main__":
    run_all_tests()
