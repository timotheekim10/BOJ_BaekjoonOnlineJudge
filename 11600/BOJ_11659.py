import sys
input = sys.stdin.readline

sum = 0
dp = [0]

n, m = map(int, input().split())
nums = list(map(int, input().split()))

for i in range(n):
    dp.append(dp[i] + nums[i])
for k in range(m):
    i, j = map(int, input().split())
    print(dp[j] - dp[i-1])
