def update_range(node, si, se, pi, pe, tree, lazy, value):
    if lazy[node] != 0:
        tree[node] += (se - si + 1) * lazy[node]
        if si != se:
            lazy[2 * node] += lazy[node]
            lazy[2 * node + 1] += lazy[node]
        lazy[node] = 0

    if ((pi < si) and (pe < si)) or ((pi > se) and (pe > se)):
        return
    elif ((pi <= si) and (pe >= se)):
        tree[node] += (se - si + 1) * value
        if se != si:
            lazy[2 * node] += value
            lazy[2 * node + 1] += value
    else:
        mid = (si + se) // 2
        update_range(2*node, si, mid, pi, pe, tree, lazy, value)
        update_range(2*node + 1, mid + 1, se, pi, pe, tree, lazy, value)
        tree[node] = tree[2*node] + tree[2*node + 1]

def get_sum(node, si, se, pi, pe, tree, lazy):
    if lazy[node] != 0:
        tree[node] += (se - si + 1) * lazy[node]
        if si != se:
            lazy[2 * node] += lazy[node]
            lazy[2 * node + 1] += lazy[node]
        lazy[node] = 0

    if (pi <= si) and (se <= pe):
        return tree[node]
    elif ((pi < si) and (pe < si)) or ((se < pi) and (se < pe)):
        return 0
    else:
        mid = (si + se) // 2
        return get_sum(2*node, si, mid, pi, pe, tree, lazy) + \
            get_sum(2*node + 1, mid + 1, se, pi, pe, tree, lazy)



t = int(input())
for _ in range(t):
    input_str = input()
    n, c = [int(x) for x in input_str.split()]
    arr = [0 for _ in range(n)]
    tree = [0 for _ in range(4 * n)]
    lazy = [0 for _ in range(4 * n)]
    for _ in range(c):
        command = input()
        if command[0] == '0':
            comm, p, q, v = [int(x) for x in command.split()]
            update_range(1, 1, n, p, q, tree, lazy, v)
        elif command[0] == '1':
            comm, p, q =  [int(x) for x in command.split()]
            print(get_sum(1, 1, n, p, q, tree, lazy))
