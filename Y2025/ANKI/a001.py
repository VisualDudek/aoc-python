# Refactor below loop into dict comprehension

data = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""

_dict = {}

for y, line in enumerate(data.splitlines()):
    for x, c in enumerate(line.strip()):
        _dict[(x,y)] = (c == "@")

print(_dict)

# Refactored using dict comprehension
_data = {}