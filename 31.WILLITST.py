def does_it_stop(n):
    nums = [n]
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 3
        if n in nums:
            return False
        nums.append(n)
    return True

n = int(input())
status = does_it_stop(n)
if status:
    print('TAK')
else:
    print('NIE')
