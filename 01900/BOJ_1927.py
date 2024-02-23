import sys
import heapq

input = sys.stdin.readline

n = int(input())

nums = []

for _ in range(n):
    x = int(input())
    if x == 0:
        if nums:
            print(heapq.heappop(nums))
        else:
            print(0)
        continue
    heapq.heappush(nums, x)