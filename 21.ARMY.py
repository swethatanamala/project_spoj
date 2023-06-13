def winning_team(godzilla, mechagodzilla):
    i, j = 0, 0
    n, m = len(godzilla), len(mechagodzilla)
    while (i < n) and (j < m):
        if godzilla[i] < mechagodzilla[j]:
            i += 1
        elif godzilla[i] > mechagodzilla[j]:
            j += 1
        else:
            j += 1
    if i == n:
        print('MechaGodzilla')
    elif j == m:
        print('Godzilla')
    else:
        print('uncertain')

t = int(input())
for _ in range(t):
    blank = input()
    input_str = input()
    ng, nm = [int(x) for x in input_str.split()]
    godzilla_str = input()
    godzilla = [int(x) for x in godzilla_str.split()]
    mechagodzilla_str = input()
    mechagodzilla = [int(x) for x in mechagodzilla_str.split()]
    godzilla, mechagodzilla = sorted(godzilla), sorted(mechagodzilla)
    winning_team(godzilla, mechagodzilla)