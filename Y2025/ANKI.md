## 001 Dict/List Comprehension - Chaining For Loops

**TIL:** You can chain multiple `for` loops in a single comprehension!

```python
# Nested loops in comprehension - outer loop comes FIRST
_data = {
    (x, y): (c == "@")
    for y, line in enumerate(data.splitlines())  # outer loop
    for x, c in enumerate(line.strip())          # inner loop
}

# This comprehension:
[x for outer in iterable1 for x in iterable2]

# Is equivalent to:
result = []
for outer in iterable1:      # first for in comprehension
    for x in iterable2:      # second for in comprehension
        result.append(x)
```

## TAKEAWAY: open file with context manger
Iterating over a file object `f` in a `with` context manager yields one line at a time.

## GOTCHA: split on `f.read()`
When you split on file e.g. `f.read().split('\n\n')` you lose magic `for line in f:` so you need to remember to `.split()` on further data.


