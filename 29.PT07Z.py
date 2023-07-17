def get_farthest_node(point, adjacency):
    nodes = len(adjacency)
    index = point
    visited = [0 for _ in range(nodes)]
    distances = [0 for _ in range(nodes)]
    visited[index] = 1
    queue = [index]
    while len(queue) > 0:
        index = queue.pop(0)
        neighbors = [i for i in adjacency[index] if (visited[i] == 0)]
        for neighbor in neighbors:
            distances[neighbor] = distances[index] + 1
            queue.append(neighbor)
            visited[neighbor] = 1
    return index, distances


nodes = int(input())
visited = [0 for _ in range(nodes)]
distances = [0 for _ in range(nodes)]
adjacency = [[] for _ in range(nodes)]
for _ in range(nodes - 1):
    input_str = input()
    m, n = [int(x) for x in input_str.split()]
    adjacency[m - 1].append(n - 1)
    adjacency[n - 1].append(m - 1)
max_index, distances = get_farthest_node(0, adjacency)
max_index, distances = get_farthest_node(max_index, adjacency)
print(max(distances))
