# simplify compute_total function using sum
# cSpell:words oneliner

from typing import List, LiteralString


input = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """

*numbers_raw, symbols_raw = input.splitlines()

symbols = symbols_raw.split()

rows = [map(int, line.split()) for line in numbers_raw]
columns: List[tuple[int, ...]] = list(zip(*rows))

def compute_total(
        columns: List[tuple[int, ...]], 
        symbols: List[LiteralString]
    ) -> int:
    from operator import mul, add
    from functools import reduce

    OPERATORS = {
        "+": add,
        "*": mul,
    }

    total = 0

    for col_values, symbol in zip(columns, symbols):
        op = OPERATORS[symbol]
        total += reduce(op, col_values)

    return total

# --- Solution ---
def compute_total_oneliner(
        columns: List[tuple[int, ...]], 
        symbols: List[LiteralString]
    ) -> int:
    from operator import mul, add
    from functools import reduce

    OPERATORS = {
        "+": add,
        "*": mul,
    }

    # CODE HERE

    return None # type: ignore


solution = compute_total(columns, symbols)
print(f"Total sum is: {solution}")

assert solution == 4277556 

solution = compute_total_oneliner(columns, symbols)
print(f"Total with operator module sum is: {solution}")

assert solution == 4277556 