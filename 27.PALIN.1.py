def greater_palindrome(input_str):
    len_n = len(input_str)
    list_inp = [int(x) for x in input_str]
    increase = True
    last = len_n // 2 if len_n % 2 else len_n // 2 - 1
    for i in range(last):
        left, right = list_inp[i], list_inp[len_n - i - 1]
        if left > right:
            list_inp[len_n - i - 1] = list_inp[i]
            increase = False
        else:
            list_inp[len_n - i - 1] = list_inp[i]
            increase = True
    if len_n % 2:
        if increase:
            list_inp[last] = list_inp[last] + 1
    else:
        if list_inp[last] > list_inp[last + 1]:
            list_inp[last + 1] = list_inp[last]
        else:
            list_inp[last] = list_inp[last] + 1
            list_inp[last + 1] = list_inp[last]
    return ''.join([str(x) for x in list_inp])


t = int(input())
for _ in range(t):
    n = input()
    greater_num = greater_palindrome(n)
    print(greater_num)