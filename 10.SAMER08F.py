def no_of_squares(n):
    result = 0
    for i in range(1, n + 1, 1):
        result += pow(i, 2)
    return result

while True:
    n = int(input())
    if n == 0:
        break
    result = no_of_squares(n)
    print(result)