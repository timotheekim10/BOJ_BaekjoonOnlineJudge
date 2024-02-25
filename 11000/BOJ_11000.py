import sys
import heapq

input = sys.stdin.readline

n = int(input())

lectures = []

for i in range(n):
    s, t = map(int, input().split())
    lectures.append([s, t])

lectures.sort()

pq = []
heapq.heappush(pq, lectures[0][1])

for i in range(1, n):
    if lectures[i][0] >= pq[0]:
        heapq.heappop(pq)
        heapq.heappush(pq, lectures[i][1])
    else:
        heapq.heappush(pq, lectures[i][1])

print(len(pq))