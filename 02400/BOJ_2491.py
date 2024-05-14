import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp_asc = [1] * n
dp_dsc = [1] * n

for i in range(0, n-1):
    if arr[i] <= arr[i+1]:
        dp_asc[i+1] = dp_asc[i] + 1

for i in range(n-1, 0, -1):
    if arr[i] <= arr[i-1]:
        dp_dsc[i-1] = dp_dsc[i] + 1

ans = max(max(dp_asc), max(dp_dsc))
print(ans)