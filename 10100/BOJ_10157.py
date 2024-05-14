import sys
from collections import deque

input = sys.stdin.readline

c, r = map(int, input().split())
k = int(input())

if k > c*r:
    print(0)
    sys.exit(0)

graph = [[False] * c for _ in range(r)]
cnt = 1

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

q = deque()
q.append((0, 0, 0, 1))
graph[0][0] = True

while q:
    y, x, d, cnt = q.popleft()
    if cnt == k:
        print(x+1, y+1)
        sys.exit(0)
    ny = y + dy[d]
    nx = x + dx[d]
    if ny < 0 or ny >= r or nx < 0 or nx >= c or graph[ny][nx]:
        nny = y+dy[(d+1)%4]
        nnx = x+dx[(d+1)%4]
        nd = (d+1)%4
        q.append((nny, nnx, nd, cnt+1))
        graph[nny][nnx] = True
    elif not graph[ny][nx]:
        q.append((ny, nx, d, cnt+1))
        graph[ny][nx] = True