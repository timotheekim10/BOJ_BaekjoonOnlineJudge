import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def bfs(sy, sx, visited, cnt_sea):
    q = deque()
    q.append((sy, sx))
    visited[sy][sx] = True

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<n and 0<=nx<m and not visited[ny][nx]:
                if graph[ny][nx] != 0:
                    q.append(((ny, nx)))
                    visited[ny][nx] = True
                else:
                    cnt_sea[y][x] += 1

year = 0

while True:
    cnt_iceberg = 0
    visited = [[False] * m for _ in range(n)]
    cnt_sea = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and not visited[i][j]:
                cnt_iceberg += 1
                bfs(i, j, visited, cnt_sea)
    for i in range(n):
        for j in range(m):
            graph[i][j] -= cnt_sea[i][j]
            if graph[i][j] < 0:
                graph[i][j] = 0
    
    if cnt_iceberg == 0:
        print(0)
        sys.exit(0)
    if cnt_iceberg >= 2:
        print(year)
        sys.exit(0)
    year += 1