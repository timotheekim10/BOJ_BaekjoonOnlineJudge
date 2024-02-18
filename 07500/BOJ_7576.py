import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*m for _ in range(n)]
queue = deque([])

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i, j])

while queue:
    y, x = queue.popleft()
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0<=ny<n and 0<=nx<m and graph[ny][nx]==0:
                queue.append([ny, nx])
                graph[ny][nx] = 1
                dp[ny][nx] = dp[y][x] + 1

day = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(-1)
            sys.exit(0)
        day = max(day, dp[i][j])

print(day)