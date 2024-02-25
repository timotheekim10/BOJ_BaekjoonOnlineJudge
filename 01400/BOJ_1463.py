import sys

input = sys.stdin.readline

x = int(input())

dp = [0] * (x+1)

for i in range(1, x):
    if dp[i+1] == 0:
        dp[i+1] = dp[i] + 1
    else:
        dp[i+1] = min(dp[i+1], dp[i]+1)
    if 2*i > x:
        continue
    if dp[2*i] == 0:
        dp[2*i] = dp[i] + 1
    else:
        dp[2*i] = min(dp[2*i], dp[i]+1)
    if 3*i > x:
        continue
    if dp[3*i] == 0:
        dp[3*i] = dp[i] + 1
    else:
        dp[3*i] = min(dp[3*i], dp[i]+1)

print(dp[x])