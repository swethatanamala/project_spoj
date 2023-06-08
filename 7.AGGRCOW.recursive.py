def get_dict(list_stall):
    map = {inp: [] for inp in list_stall}
    for ind, inp in enumerate(list_stall):
        for i in range(ind + 1, len(list_stall), 1):
            map[inp].append(list_stall[i] - inp)
    return map

def helper(map, key, steps, min_num):
    if steps == 1:
        max_num = 0
        for num in map[key]:
            max_num = max(max_num, num)
        min_num = min(min_num, max_num)
        return min_num
    else:
        max_num = 0
        for num in map[key]:
            max_num = max(max_num, helper(map, key + num, steps - 1, num))
        min_num = min(min_num, max_num)
        return min_num        

t = int(input())
for _ in range(t):
    inp_str = input()
    n, cows = [int(x) for x in inp_str.split(' ')]
    stalls = []
    for _ in range(n):
        stall = int(input())
        stalls.append(stall)
    stalls = sorted(stalls)
    map = get_dict(stalls)
    min_num = helper(map, stalls[0], cows - 1, 1000000000)
    print(min_num)