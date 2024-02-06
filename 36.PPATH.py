def get_lower_primes(high):
    primes = [True for _ in range(high)]
    for i in range(2, int(pow(high, 0.5))):
        if primes[i]:
            for num in range(i * i, high, i):
                primes[num] = False
    return [num for num in range(high) if primes[num]]

def get_primes(low, high):
    primes_list = get_lower_primes(high)
    primes_list = [num for num in primes_list if num > 1000]
    return primes_list

def is_connected(x, y):
    str_x = str(x)
    str_y = str(y)
    return ((str_x[0] != str_y[0]) & (str_x[1] == str_y[1]) & (str_x[2] == str_y[2]) & (str_x[3] == str_y[3]) or
            (str_x[0] == str_y[0]) & (str_x[1] != str_y[1]) & (str_x[2] == str_y[2]) & (str_x[3] == str_y[3]) or
            (str_x[0] == str_y[0]) & (str_x[1] == str_y[1]) & (str_x[2] != str_y[2]) & (str_x[3] == str_y[3]) or
            (str_x[0] == str_y[0]) & (str_x[1] == str_y[1]) & (str_x[2] == str_y[2]) & (str_x[3] != str_y[3]))

def get_graph(primes_list):
    prime_len = len(primes_list)
    mat = [[0 for _ in range(prime_len)] for _ in range(prime_len)]
    for i in range(prime_len):
        for j in range(i + 1, prime_len):
            mat[i][j] = is_connected(primes_list[i], primes_list[j])
            mat[j][i] = mat[i][j]
    return mat

def get_short_path(source, dest, primes_list, mat):
    if source == dest:
        return 0
    dist = [-1 for _ in primes_list]
    visited = [0 for _ in primes_list]
    source_ind = primes_list.index(source)
    visited[source_ind] = 1
    dist[source_ind] = 0
    dest_ind = primes_list.index(dest)
    queue = []
    queue.append(source_ind)
    while len(queue) > 0:
    # for i in range(len(primes_list)):
        source_ind = queue.pop(0)
        adjacent_vertices = [i for i in range(len(primes_list)) if mat[source_ind][i]]
        for i in adjacent_vertices:
            if mat[source_ind][i]:
                if not visited[i]:
                    dist[i] = dist[source_ind] + 1
                    visited[i] = 1
                    queue.append(i)
                    if i == dest_ind:
                        return dist[dest_ind]
    return dist[dest_ind]
t = int(input())
primes = get_primes(1000, 10000)
#print(primes)
mat = get_graph(primes)
for _ in range(t):
    input_str = input()
    source, dest = [int(x) for x in input_str.split()]
    dist = get_short_path(source, dest, primes, mat)
    print(dist)
