import sys
input = sys.stdin.readline

count = 0

N = int(input())
nums = list(map(int, input().split()))
v = int(input())

for num in nums:
    if num == v:
        count += 1

print(count)
