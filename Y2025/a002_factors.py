FACTORS = {1: [], 2: [1], 3: [1], 4: [2, 1], 5: [1], 6: [3, 2, 1], 7: [1], 8: [4, 2, 1], 9: [3, 1], 10: [5, 2, 1]}
p1 = p2 = 0
with open("puzzle_input/002.txt", mode="r", encoding="utf-8") as f:
    for n1, n2 in [i.split("-") for i in f.read().strip().split(",")]:
        for i in range(int(n1), int(n2) + 1):
            size = len(str(i))
            for r in FACTORS[size]:
                if len(set(str(i)[j:j + r] for j in range(0, size, r))) == 1:
                    p1 += i * (r * 2 == size)
                    p2 += i
                    break
print(f"Part 1: {p1}\nPart 2: {p2}")