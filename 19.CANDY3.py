t = int(input())
for _ in range(t):
    line = input()
    n = int(input())
    candies = []
    for _ in range(n):
        x = int(input())
        candies.append(x)
    if sum(candies) % n == 0:
        print('YES')
    else:
        print('NO')