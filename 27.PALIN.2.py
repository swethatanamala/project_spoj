def greater_palindrome(input_str):
    len_n = len(input_str)
    last = len_n // 2 - 1
    list_inp = [int(x) for x in input_str]
    middle, sub = None, 1
    if len_n % 2:
        middle = list_inp[last + 1]
        sub += 1
    is_equal = True
    while last >= 0:
        if list_inp[last] < list_inp[last + sub]:
            if middle:
                middle += 1
            else:
                list_inp[last] += 1
            is_equal = False
            break
        elif list_inp[last] > list_inp[last + sub]:
            is_equal = False
            break
        last -= 1
    if is_equal:
        if list_inp[0] == 9:
            return '1' + '0' * (len_n - 1) + '1'
        elif list_inp[0] == 0:
            return '1'
        if len_n % 2:
            middle += 1
        else:
            list_inp[len_n//2 - 1] = list_inp[len_n//2 - 1] + 1
    first_half = ''.join([str(x) for x in list_inp[:len_n//2]])
    if middle:
        return first_half + str(middle) + first_half[::-1]
    else:
        return first_half + first_half[::-1]
    

t = int(input())
for _ in range(t):
    n = input()
    greater_num = greater_palindrome(n)
    print(greater_num)