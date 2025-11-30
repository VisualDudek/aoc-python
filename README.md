# aoc-python
Python solutions for Advent of Code challenges
<!-- cSpell:ignore adventofcode megathreads defaultdict  -->
## Source
- Challenges from [Advent of Code](https://adventofcode.com/)
- Community discussions on [r/adventofcode](https://www.reddit.com/r/adventofcode/) - features solution megathreads where exceptional solutions can be found

## Python-Specific Techniques Used

### Collections Module
- **`Counter`**: Efficient frequency counting for similarity score calculations
  - Example: `Counter(right)` creates a dictionary with element counts
  - Used in [a001B.py:27](Y2024/a001B.py#L27)

- **`defaultdict`**: Dictionary with default values, eliminates key existence checks
  - Example: `defaultdict(int)` auto-initializes missing keys to 0
  - Used in [a001B.py:37](Y2024/a001B.py#L37)

### Dictionary Methods
- **`dict.get(key, default)`**: Safe dictionary access with fallback value
  - Example: `right_dict.get(l, 0)` returns 0 if key doesn't exist
  - Cleaner than `if key in dict` checks
  - Used in [a001B.py:54](Y2024/a001B.py#L54) and [a001B.py:58](Y2024/a001B.py#L58)

### Data Processing
- **Tuple unpacking**: Clean data extraction from structured data
  - Example: `left, right = data`
  - Used throughout [a001B.py](Y2024/a001B.py)

### Design Patterns
- **Callable types**: Functions as parameters for strategy pattern
  - Example: `Callable[[utils.Data], int]` in [a001B.py:17](Y2024/a001B.py#L17)
  - Allows flexible solution implementations
