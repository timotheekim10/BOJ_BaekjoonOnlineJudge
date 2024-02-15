import sys

input = sys.stdin.readline

dp = [[1,0], [0, 1]]

t = int(input())

for _ in range(t):
    n = int(input())
    if n==0 or n==1:
        print(dp[n][0], dp[n][1])
    else:
        for i in range(2, n+1):
            if len(dp) <= i:
                dp.append([dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1]])
        print(dp[n][0], dp[n][1])