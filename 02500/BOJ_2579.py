import sys

input = sys.stdin.readline

stairs = [0]
dp = [0] * 301

n = int(input())

for i in range(n):
    stairs.append(int(input()))

dp[1] = stairs[1]
if n == 1:
    print(dp[1])
    sys.exit(0)
dp[2] = stairs[1] + stairs[2]
if n == 2:
    print(dp[2])
    sys.exit(0)
for i in range(3, n+1):
    dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])

print(dp[n])