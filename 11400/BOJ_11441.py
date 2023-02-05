import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

prefixSum = [0]
sum = 0

for num in A:
    sum += num
    prefixSum.append(sum)

M = int(input())
for _ in range(M):
    i, j = map(int, input().split())
    print(prefixSum[j]-prefixSum[i-1])
