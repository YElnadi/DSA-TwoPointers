def solution (a):
    pairs = {}
    count = 0
    for num in a:
        sorted_nums = ''.join(sorted(str(num)))
        if sorted_nums not in pairs:
            pairs[sorted_nums] = 0
        pairs[sorted_nums] += 1

    for value in pairs.values():
        if value >= 2:
            count += (value * (value - 1)) // 2

    print(count)
        





















print(solution([25, 35, 872, 228, 53, 278, 872]))