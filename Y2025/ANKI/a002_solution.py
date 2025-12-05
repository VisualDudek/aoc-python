# Split data into two parts
# next split ranges using list comprehension

data = """3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""


ranges, ids = data.split("\n\n")

ranges_processed = [tuple(map(int, line.split("-"))) for line in ranges.strip().splitlines()]

# This is crazy example of list comprehension

ranges_crazy = ([int(x) for x in line.split("-")] for line in ranges.strip().splitlines())

print(ranges_processed)
print(list(ranges_crazy))