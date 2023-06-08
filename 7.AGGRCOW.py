def get_min_max(stalls, cows):
    left, right = 1, 1000000001
    min_max = 1
    while left < right:
        mid = (left + right)//2
        count, n, prev = 1, len(stalls), stalls[0]
        for i in range(1, n, 1):
            if (stalls[i] - prev) >= mid:
                count += 1
                prev = stalls[i]
        if count < cows:
            right = mid
        else:
            min_max = max(min_max, mid)
            left = mid + 1
    return min_max

t = int(input())
for _ in range(t):
    inp_str = input()
    n, cows = [int(x) for x in inp_str.split(' ')]
    stalls = []
    for _ in range(n):
        stall = int(input())
        stalls.append(stall)
    stalls = sorted(stalls)
    min_max = get_min_max(stalls, cows)
    print(min_max)