import sys
import heapq

input = sys.stdin.readline

n = int(input())

nums = []

for i in range(n):
    num = int(input())
    if num == 0:
        if nums:
            print(heapq.heappop(nums)[1])
        else:
            print(0)
        continue
    heapq.heappush(nums, (-num, num))