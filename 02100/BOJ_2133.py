import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * (n+1)

if n % 2:
    print(0)
else:
    dp[2] = 3
    for i in range(4, n+1, 2):
        dp[i] = dp[i-2] * 3 + 2
        for j in range(2, i-2, 2):
            dp[i] += dp[j] * 2
    print(dp[-1])