def num_zeros(n):
    i = 1
    result = 0
    while True:
        div = n//pow(5, i)
        if div == 0:
            break
        result += div
        i += 1
    return result

t = input()
for _ in range(int(t)):
    n = int(input())
    result = num_zeros(n)
    print(result)