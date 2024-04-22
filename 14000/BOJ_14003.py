import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

LIS = [a[0]]
dp = [(0, a[0])]

def binary_search(x):
    start, end = 0, len(LIS) - 1
    while start <= end:
        mid = (start + end) // 2
        if LIS[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
    return start

for i in range(n):
    if LIS[-1] < a[i]:
        LIS.append(a[i])
        dp.append((len(LIS)-1, a[i]))
    else:
        idx = binary_search(a[i])
        LIS[idx] = a[i]
        dp.append((idx, a[i]))

last_idx = len(LIS) - 1
ans = []
for i in range(len(dp)-1, -1, -1):
    if dp[i][0] == last_idx:
        ans.append(dp[i][1])
        last_idx -= 1

print(len(LIS))
print(*ans[::-1])