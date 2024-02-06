def generateNextPalindrome(list_num, n):
    if (len(set(list_num)) == 1) and (list_num[0] == 9):
        print('1' + '0' * (n - 1) + '1')
    else:
        mid = n // 2
        i = mid - 1
        j = mid + 1 if n % 2 else mid
        while i >= 0:
            if list_num[i] == list_num[j]:
                i -= 1
                j += 1
        smaller = False
        if (i < 0) or (list_num[i] < list_num[j]):
            smaller = True
        if smaller == True:
            i = mid - 1
            carry = 1
            if n % 2:
                j = mid + 1
                list_num[mid] = list_num[mid] + carry
                carry = list_num[mid] // 10
                list_num[mid] = list_num[mid] % 10
            else:
                j = mid
            while i >= 0:
                list_num[i] = list_num[i] + carry
                carry = list_num[i] // 10
                list_num[i] = list_num[i] % 10
                list_num[j] = list_num[i]
                j += 1
                i -= 1
        print("".join([str(x) for x in list_num]))

t = int(input())
for _ in range(t):
    num = input()
    list_num = [int(x) for x in num]
    n = len(num)
    generateNextPalindrome(list_num, n)