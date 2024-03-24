import sys
from collections import deque

input = sys.stdin.readline

n, m, t = map(int, input().split())

visited = [[False]*m for _ in range(n)]
graph = [list(map(int, input().split())) for _ in range(n)]
ans = 1e9
gram = False

queue = deque([])
queue.append([0, 0, 0])
visited[0][0] = True

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

while queue:
    y, x, h = queue.popleft()
    if y==n-1 and x==m-1:
        ans = min(ans, h)
        if ans <= t:
            print(ans)
            sys.exit(0)
        else:
            print('Fail')
            sys.exit(0)
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0<=ny<n and 0<=nx<m and not visited[ny][nx]:
            if graph[ny][nx] == 0:
                visited[ny][nx] = True
                queue.append([ny, nx, h+1])
                continue
            if graph[ny][nx] == 2:
                visited[ny][nx] = True
                queue.append([ny, nx, h+1])
                ans = (h+1)+(n-1-ny)+(m-1-nx)
                gram = True

if gram:
    if ans <= t:
        print(ans)
    else:
        print('Fail')
else:
    print('Fail')