import sys

input = sys.stdin.readline

n, m = map(int, input().split())
data = []

for _ in range(m):
    day, page = map(int, input().split())
    data.append([day, page])

dp = [[0]*(n+1) for _ in range(m+1)]

for i in range(1, m+1):
    for j in range(1, n+1):
        if j >= data[i-1][0]:
            dp[i][j] = max(dp[i-1][j-data[i-1][0]] + data[i-1][1], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
    
print(dp[m][n])