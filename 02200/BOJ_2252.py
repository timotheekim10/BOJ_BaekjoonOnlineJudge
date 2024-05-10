import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
temp = [0] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    temp[b] += 1

q = deque()

for s in range(1, n+1):
    if temp[s] == 0:
        q.append(s)

ans = []

while q:
    s = q.popleft()
    ans.append(s)
    for adj_s in graph[s]:
        temp[adj_s] -= 1
        if temp[adj_s] == 0:
            q.append(adj_s)

print(*ans)