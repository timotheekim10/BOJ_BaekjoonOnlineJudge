import sys

input = sys.stdin.readline

n = int(input())
s = input().rstrip()

dp = [0]*(n+1)
dp[0] = 1

for i in range(1, n+1):
    dp[i] = dp[i-1]
    if i>=8 and s[i-8:i]=='longlong':
        dp[i] += dp[i-8]

print(dp[n])