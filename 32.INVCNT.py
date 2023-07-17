# def get_inv_count(n, arr):
#     count = 0
#     for i in range(1, n):
#         key = arr[i]
#         left, right = 0, i 
#         while left < right:
#             mid = (left + right) // 2
#             if arr[mid] < key:
#                 left = mid + 1
#             else:
#                 right = mid
#         if left != i:
#             count += (i - left)
#             arr[left + 1:i + 1] = arr[left:i]
#             arr[left] = key
#     return count

def merge(arr, l, mid, r, count):
    n1 = mid + 1 - l
    n2 = r - mid
    a = arr[l : mid + 1]
    b = arr[mid + 1 : r + 1]
    i, j = l, mid + 1
    while (i <= mid) and (j <= r):
        if b[j - r] < a[i - mid]:
            arr[i] = arr[j]


t = int(input())
blank_space = input()
for _ in range(t):
    n = int(input())
    nums = []
    for _ in range(n):
        num = int(input())
        nums.append(num)
    blank_space = input()
    inv_count = get_inv_count(n, nums)
    print(inv_count)
