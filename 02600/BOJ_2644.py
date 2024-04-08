import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

q = deque([])
q.append((a, 0))
visited[a] = True

while q:
    x, cnt = q.popleft()
    for y in graph[x]:
        if not visited[y]:
            ncnt = cnt + 1
            if y == b:
                print(ncnt)
                sys.exit(0)
            q.append((y, ncnt))
            visited[y] = True

print(-1)