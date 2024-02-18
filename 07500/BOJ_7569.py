import sys
from collections import deque

input = sys.stdin.readline

m, n, h = map(int, input().split())

graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
dp = [[[0]*m for _ in range(n)] for _ in range(h)]
queue = deque([])

print(graph)

dz = [0, 0, 0, 0, 1, -1]
dy = [1, -1, 0, 0, 0, 0]
dx = [0, 0, 1, -1, 0, 0]

for i in range(h):  
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                queue.append([i, j, k])

while queue:
    z, y, x = queue.popleft()
    for i in range(6):
        nz, ny, nx = z + dz[i], y + dy[i], x + dx[i]
        if 0<=nz<h and 0<=ny<n and 0<=nx<m and graph[nz][ny][nx]==0:
                queue.append([nz, ny, nx])
                graph[nz][ny][nx] = 1
                dp[nz][ny][nx] = dp[z][y][x] + 1

day = 0

for i in range(h):
     for j in range(n):
          for k in range(m):
            if graph[i][j][k] == 0:
                print(-1)
                sys.exit(0)
            day = max(day, dp[i][j][k])

print(day)