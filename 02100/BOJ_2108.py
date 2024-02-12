import sys
from collections import Counter

input = sys.stdin.readline

nums = []

n = int(input())

for _ in range(n):
    nums.append(int(input()))

nums.sort()

print(round(sum(nums)/n))
print(nums[n//2])
temp = Counter(nums).most_common()
if n == 1:
    print(nums[0])
else:
    if temp[0][1] == temp[1][1]:
        print(temp[1][0])
    else:
        print(temp[0][0])
print(nums[-1]-nums[0])