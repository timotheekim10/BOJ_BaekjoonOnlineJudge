import sys
import heapq

input = sys.stdin.readline

n = int(input())

nums = []

for _ in range(n):
    x = int(input())
    if x == 0:
        if nums:
            print(heapq.heappop(nums)[1])
        else:
            print(0)
        continue
    if x > 0:
        heapq.heappush(nums, (x, x))
    else:
        heapq.heappush(nums, (-x, x))