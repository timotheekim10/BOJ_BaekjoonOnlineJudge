import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [input().strip() for _ in range(n)]
visited = [[[0]*(k+1) for _ in range(m)] for _ in range(n)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

q = deque([])
q.append((0, 0, k))
visited[0][0][k] = 1

while q:
    y, x, z = q.popleft()
    if y==n-1 and x==m-1:
        print(visited[y][x][z])
        sys.exit(0)
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0<=ny<n and 0<=nx<m:
            if graph[ny][nx]=='1' and visited[ny][nx][z-1]==0 and z>0:
                visited[ny][nx][z-1] = visited[y][x][z] + 1
                q.append((ny, nx, z-1))
            elif graph[ny][nx]=='0' and visited[ny][nx][z]==0:
                visited[ny][nx][z] = visited[y][x][z] + 1
                q.append((ny, nx, z))
print(-1)