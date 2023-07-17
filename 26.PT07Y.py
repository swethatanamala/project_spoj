input_str = input()
m, n = [int(x) for x in input_str.split()]
is_visited = [0 for _ in range(m)]
is_tree = 1
for _ in range(n):
    edge = input()
    edge_i, edge_j = [int(x) for x in edge.split()]
    if is_visited[edge_j - 1]:
        print('NO')
        is_tree = 0
        break
    is_visited[edge_i - 1] = 1
    is_visited[edge_j - 1] = 1
if is_tree:
    print('YES')