t = int(input())
for _ in range(t):
    n = int(input())
    men_input_str = input()
    men = sorted([int(x) for x in men_input_str.split()])
    women_input_str = input()
    women = sorted([int(x) for x in women_input_str.split()])
    result = 0
    for i in range(n):
        result += men[i] * women[i]
    print(result)