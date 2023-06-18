t = int(input())
for _ in range(t):
    input_str = input()
    x, y, sum = [int(x) for x in input_str.split()]
    n = 2 * sum//(x + y)
    d = (y - x)/(n - 5)
    a = (x - 2 * d)
    print(n)
    for i in range(n):
        print(int(a + i * d), end=' ')
    print()
    