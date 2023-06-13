
same_digits = [0, 1, 5, 6]
t = int(input())
for _ in range(t):
    input_str = input()
    base, ind = [int(x) for x in input_str.split()]
    if ind == 0:
        print(1)
    elif base % 10 in same_digits:
        print(base % 10)
    else:
        last_digit = base % 10
        if (ind % 4 == 0):
            print(pow(last_digit, 4) % 10)
        else:
            print(pow(last_digit, ind % 4) % 10)