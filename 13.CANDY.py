def move_candies(candies):
    total = sum(candies)
    if total % len(candies) != 0:
        return -1
    mean = total / len(candies)
    to_move = 0
    for candy in candies:
        if candy < mean:
            to_move += (mean - candy)
    return to_move

while True:
    n = int(input())
    if n == -1:
        break
    candies = []
    for _ in range(n):
        element = int(input())
        candies.append(element)
    to_move = move_candies(candies)
    print(int(to_move))
