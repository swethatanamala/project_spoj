# your code goes here
# your code goes here
def edit_distance(a, b):
	n = len(a)
	m = len(b)
	prev = [j for j in range(m+1)]
	curr = [0] * (m+1)
	for i in range(1, n+1):
		curr[0] = i
		for j in range(1, m+1):
			if a[i-1] == b[j-1]:
				curr[j] = prev[j-1]
			else:
				mn = min(1 + prev[j], 1 + curr[j-1])
				curr[j] = min(mn, 1 + prev[j-1])
		prev = curr.copy()
	return prev[m]


t = int(input())

for _ in range(t):
    a = input()
    b = input()
    distance = edit_distance(a, b)
    print(distance)