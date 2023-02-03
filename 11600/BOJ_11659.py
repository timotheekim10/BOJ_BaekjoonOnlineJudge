import sys
input = sys.stdin.readline

sum = 0
prefixSum = [0]

n, m = map(int, input().split())
nums = list(map(int, input().split()))

for i in range(n):
    sum += nums[i]
    prefixSum.append(sum)
for k in range(m):
    i, j = map(int, input().split())
    print(prefixSum[j] - prefixSum[i-1])
