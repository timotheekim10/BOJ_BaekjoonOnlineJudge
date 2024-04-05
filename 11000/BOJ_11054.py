import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

dp_asc = [1]*n
dp_dsc = [1]*n
dp = [0]*n

for i in range(1, n):
    for j in range(i):
        if a[i] > a[j]:
            dp_asc[i] = max(dp_asc[i], dp_asc[j]+1)

for i in range(n-2, -1, -1):
    for j in range(i+1, n):
        if a[i] > a[j]:
            dp_dsc[i] = max(dp_dsc[i], dp_dsc[j]+1)

for i in range(n):
    dp[i] = dp_asc[i] + dp_dsc[i] - 1

print(max(dp))