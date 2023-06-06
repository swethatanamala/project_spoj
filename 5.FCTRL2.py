def factorial(n):
    result_fac = [1 for _ in range(n + 1)]
    for i in range(n):
        result_fac[i + 1] = (i + 1) * result_fac[i]
    return result_fac[-1]

t = input()
for _ in range(int(t)):
    n = int(input())
    print(factorial(n))