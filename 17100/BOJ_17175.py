import sys

input = sys.stdin.readline

n = int(input())

dp = [1]*(n+2)

if n==0 or n==1:
    print(dp[n])
    sys.exit(0)
else:
    for i in range(2, n+1):
        dp[i] += dp[i-1] + dp[i-2]

print(dp[n]%1000000007)