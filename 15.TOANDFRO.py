def decode_message(input_str, cols):
    rows = len(input_str)//n
    matrix = [['' for _ in range(cols)] for _ in range(rows)]
    for i in range(0, len(input_str), cols):
        if ((i) % 2) == 0:
            for j in range(cols):
                matrix[i//cols][j] = input_str[i + j]
        else:
            for j in range(cols - 1, -1, -1):
                matrix[i//cols][cols - j - 1] = input_str[i + j]
        print(matrix)
    for row_i in range(rows - 1, -1, -1):
        if matrix[row_i][cols - 1] == 'x':
            matrix[row_i][cols - 1] = ''
        else:
            break
    result = ''
    for col_i in range(cols):
        for row_i in range(rows):
            result += matrix[row_i][col_i]
    return result

while True:
    n = int(input())
    if n == 0:
        break
    input_str = input()
    result = decode_message(input_str, n)
    print(result)
