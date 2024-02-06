def edit_distance(str1, str2):
    rows, cols = len(str1), len(str2)
    mat = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]
    for i in range(cols + 1):
        mat[rows][i] = 10000
    for j in range(rows + 1):
        mat[j][cols] = 10000
    for i in reversed(range(rows)):
        for j in reversed(range(cols)):
            if (i == rows - 1) and (j == cols - 1):
                if str1[i] == str2[j]:
                    mat[i][j] = 0
                else:
                    mat[i][j] = 1
            elif str1[i] == str2[j]:
                mat[i][j] = mat[i + 1][j + 1]
            else:
                mat[i][j] = 1 + min(mat[i + 1][j], mat[i + 1][j + 1], mat[i][j + 1])
    return mat[0][0]

t = int(input())
for i in range(t):
    str1 = input()
    str2 = input()
    print(edit_distance(str1, str2))