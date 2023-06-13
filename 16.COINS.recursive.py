import sys
def get_american_dollars(n, map):
    if n == 0:
        map[n] = 0
        return map[n]
    elif n in map:
        return map[n]
    else:
        map[n] = max(n, get_american_dollars(n//2, map) + 
                        get_american_dollars(n//3, map) + 
                        get_american_dollars(n//4, map))
        return map[n]

for line in sys.stdin:
    map = {}
    print(get_american_dollars(int(line), map))