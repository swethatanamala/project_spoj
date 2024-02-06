def edit_distancecheck(str1, str2):
    if len(str1) == 0:
        return len(str2)
    elif len(str2) == 0:
        return len(str1)
    elif str1[0] == str2[0]:
        return edit_distancecheck(str1[1:], str2[1:])
    else:
        return 1 + min(edit_distancecheck(str1[1:], str2),
                        edit_distancecheck(str1[1:], str2[1:]),
                        edit_distancecheck(str1, str2[1:]))

t = int(input())
for i in range(t):
    str1 = input()
    str2 = input()
    if len(str1) <= len(str2):
        print(edit_distancecheck(str1, str2))
    else:
        print(edit_distancecheck(str2, str1))
