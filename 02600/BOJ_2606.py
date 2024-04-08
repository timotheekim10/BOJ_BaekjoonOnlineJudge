import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
k = int(input())

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(k):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque()
q.append(1)
visited[1] = True

cnt = 0

while q:
    a = q.popleft()
    for b in graph[a]:
        if not visited[b]:
            q.append(b)
            visited[b] = True
            cnt += 1

print(cnt)