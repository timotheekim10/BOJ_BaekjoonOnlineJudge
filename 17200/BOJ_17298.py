import sys

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

nge = [-1] * n
stack = [0]

for i in range(1, n):
    while stack and nums[stack[-1]] < nums[i]:
        nge[stack.pop()] = nums[i]
    stack.append(i)

print(*nge)