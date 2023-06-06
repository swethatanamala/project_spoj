
def reverse_num(num):
    result = 0
    while num != 0:
        result = result * 10 + num % 10
        num = num // 10
    return result

t = input()
for _ in range(int(t)):
    input_str = input()
    first, second = [int(x) for x in input_str.split(' ')]
    first, second = reverse_num(first), reverse_num(second)
    print(reverse_num(first + second))
