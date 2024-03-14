import sys

input = sys.stdin.readline

d, k = map(int, input().split())

dp = [0]*(d+1)

dp[1], dp[2] = 1, 1

while True:
    for i in range(3, d+1):
        dp[i] = dp[i-1] + dp[i-2]
    if dp[d] == k:
        print(dp[1])
        print(dp[2])
        break
    elif dp[d] > k:
        dp[1], dp[2] = dp[1]+1, dp[1]
    else:
        dp[2] += 1