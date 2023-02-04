import sys
input = sys.stdin.readline

sum = 0

N = int(input())
nums = input()

for i in range(N):
    sum += int(nums[i])

print(sum)
