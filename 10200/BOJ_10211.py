import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    x = list(map(int, input().split()))
    dp = [0]*(n+1)
    arr = []
    for i in range(1, n+1):
        dp[i] += dp[i-1] + x[i-1]
    for j in range(n, 0, -1):
        max_val = float('-inf')
        for k in range(j-1, -1, -1):
            max_val = max(max_val, dp[j]-dp[k])
        arr.append(max_val)
    print(max(arr))