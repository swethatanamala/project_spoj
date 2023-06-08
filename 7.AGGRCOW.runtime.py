last_xn = 1000000000

def get_right(stalls, num, left):
    right = len(stalls)
    while left < right:
        mid = (left + right)//2
        if num <= stalls[mid]:
            right = mid
        else:
            left = mid + 1
    return right

def can_place(stalls, cows, i, diff):
    print(stalls, cows, i, diff)
    num = stalls[i] + diff
    if cows == 0:
        return True
    elif i == len(stalls) - 1:
        return False
    else:
        right = get_right(stalls, num, i + 1)
        if right == len(stalls):
            return False
        else:
            return can_place(stalls, cows - 1, right, diff)
        

def get_max_min_distance(stalls, cows):
    min_max = 1
    for i in range(2, last_xn, 1):
        if can_place(stalls, cows - 1, 0, i):
            min_max = max(min_max, i)
        else:
            break
    return min_max

t = int(input())
for _ in range(t):
    inp_str = input()
    n, cows = [int(x) for x in inp_str.split()]
    stalls = []
    for _ in range(n):
        stall = int(input())
        stalls.append(stall)
    stalls = sorted(stalls)
    min_max = get_max_min_distance(stalls, cows)
    print(min_max)
