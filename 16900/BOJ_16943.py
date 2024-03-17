import sys
from itertools import permutations

input = sys.stdin.readline

a, b = input().split()
b = int(b)
c = -1

nums = []

for num in permutations(a):
    nums.append(''.join(num))

for num in nums:
    if num[0] == '0':
        continue
    num = int(num)
    if num < b:
        c = max(c, num)

print(c)