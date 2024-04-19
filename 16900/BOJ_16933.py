import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [input().strip() for _ in range(n)]
visited = [[[False]*(k+1) for _ in range(m)] for _ in range(n)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

q = deque()
q.append((0, 0, k, 1))
visited[0][0][k] = True

while q:
    y, x, z, dis = q.popleft()
    if y==n-1 and x==m-1:
        print(dis)
        sys.exit(0)
    day = dis%2
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        nz = z - 1
        if 0<=ny<n and 0<=nx<m:
            if graph[ny][nx]=='0' and not visited[ny][nx][z]:
                q.append((ny, nx, z, dis+1))
                visited[ny][nx][z] = True
            if graph[ny][nx]=='1' and not visited[ny][nx][nz] and z>0:
                if day:
                    visited[ny][nx][nz] = True
                    q.append((ny, nx, nz, dis+1))
                else:
                    q.append((y, x, z, dis+1))

print(-1)