def get_min_cards(sum):
    num = 2
    while True:
        sum = sum - (1/num)
        if sum <= 0:
            break
        num += 1
    return num - 1

while True:
    sum = float(input())
    if sum == 0:
        break
    print(f'{get_min_cards(sum)} card(s)')
