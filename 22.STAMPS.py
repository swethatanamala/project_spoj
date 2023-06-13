def number_of_friends(need, stamps):
    stamps = sorted(stamps, reverse=True)
    friends = 0
    for stamp in stamps:
        if need <= 0:
            break
        need -= stamp
        friends += 1
    return friends, need


t = int(input())
for i in range(t):
    input_str = input()
    need, length = [int(x) for x in input_str.split()]
    stamps_str = input()
    stamps = [int(x) for x in stamps_str.split()]
    friends, need = number_of_friends(need, stamps)
    print(f'Scenario #{str(i + 1)}:')
    if need > 0:
        print('impossible')
    else:
        print(friends)
