def get_888(n):
    n = n - 1
    decodes = [192, 442, 692, 942]
    div = n // 4
    rem = n % 4
    return div * 1000 + decodes[rem]


t = int(input())
for _ in range(t):
    n = int(input())
    result = get_888(n)
    print(result)