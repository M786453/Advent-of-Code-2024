from collections import Counter

stones = Counter(map(int, '2701 64945 0 9959979 93 781524 620 1'.split()))

for blinks in range(1, 76):
    new_stones = Counter()
    for n, num_stone in stones.items():
        mid, rem = divmod(len(str(n)), 2)
        if n == 0:
            new_stones[1] += num_stone
        elif rem:
            new_stones[2024 * n] += num_stone
        else:
            for m in divmod(n, 10**mid):
                new_stones[m] += num_stone
    stones = new_stones
    if blinks in (25, 75):
        print(sum(new_stones.values()))