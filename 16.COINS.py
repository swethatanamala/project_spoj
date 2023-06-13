import sys
def get_american_dollars(n):
    dp = [0 for _ in range(n + 1)]
    for i in range(1, n + 1, 1):
        dp[i] = max(i, dp[i//2] + dp[i//3] + dp[i//4])

    return dp[n]

for line in sys.stdin:
    print(get_american_dollars(int(line)))