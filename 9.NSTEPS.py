t = input()
for _ in range(int(t)):
    input_str = input()
    x, y = [int(i) for i in input_str.split()]
    if x == y:
        if x % 2 == 0:
            print(x * 2)
        else:
            print(x * 2 - 1)
    elif (y == (x - 2)):
        if x % 2 == 0:
            print(x + y)
        else:
            print(x + y - 1)
    else:
        print('No Number')