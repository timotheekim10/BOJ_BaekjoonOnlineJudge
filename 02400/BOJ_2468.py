import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

max_val = 0

for i in range(n):
    max_val = max(max_val, max(graph[i]))

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def bfs(sy, sx, val, visited):
    q = deque([])
    q.append((sy, sx))
    visited[sy][sx] = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<n and 0<=nx<n and graph[ny][nx]>val and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((ny, nx))

ans = 0

for val in range(max_val):
    visited = [[False] * n for _ in range(n)]
    cnt = 0
    for j in range(n):
        for k in range(n):
            if graph[j][k] > val and not visited[j][k]:
                bfs(j, k, val, visited)
                cnt += 1
    ans = max(ans, cnt)

print(ans)