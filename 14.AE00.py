MAX = 100
def get_unique_rectangles(n):
    rectangles = n
    for i in range(2, MAX + 1, 1):
        if i * i == n:
            rectangles += 1
        elif i * i > n:
            break
        else:
            remainder = n - (i * i)
            rectangles += (remainder // i) + 1
    return rectangles

n = int(input())
rectangles = get_unique_rectangles(n)
print(rectangles)
