import sys
input = sys.stdin.readline

sum = 0
prefixSum = [0]
max = float('-inf')

n, k = map(int, input().split())
nums = list(map(int, input().split()))

for i in range(n):
    sum += nums[i]
    prefixSum.append(sum)
for i in range(k, len(prefixSum)):
    if prefixSum[i] - prefixSum[i-k] > max:
        max = prefixSum[i] - prefixSum[i-k]
print(max)
