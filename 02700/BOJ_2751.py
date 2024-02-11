import sys
input = sys.stdin.readline

nums = []

n = int(input())

for _ in range(n):
    nums.append(int(input()))

nums.sort()

for num in nums:
    print(num)