def decode(input_str, n):
    m = len(input_str) // n
    message = [['' for i in range(n)] for j in range(m)]
    for i in range(len(input_str)):
        row_i = i // n
        col_i = i % n
        if row_i%2 == 0:
            message[row_i][col_i] = input_str[i]
        else:
            message[row_i][n - 1 - col_i] = input_str[i]
    result = ''
    for j in range(n):
        for i in range(m):
            result += message[i][j]
    return result


while True:
    n = int(input())
    if n == 0:
        break
    input_str = input()
    print(decode(input_str, n))

