import sys
from collections import deque

input = sys.stdin.readline

def pipe_dir(pipe):
    if pipe == '|':
        return [0, 1]
    elif pipe == '-':
        return [2, 3]
    elif pipe == '+' or pipe == 'M' or pipe == 'Z':
        return [0, 1, 2, 3]
    elif pipe == '1':
        return [1, 3]
    elif pipe == '2':
        return [0, 3]
    elif pipe == '3':
        return [0, 2]
    elif pipe == '4':
        return [1, 2]
    
def bfs(sy, sx, sdir):
    global fy, fx
    q = deque()
    q.append([sy, sx, sdir])
    visited[sy][sx] = True
    while q:
        y, x, dir = q.popleft()
        for d in dir:
            ny = y + dy[d]
            nx = x + dx[d]
            nd = (d+1)%2 if d<2 else (d+1)%2+2
            if 0<=ny<r and 0<=nx<c and not visited[ny][nx]:
                if graph[ny][nx] != '.':
                    visited[ny][nx] = True
                    q.append([ny, nx, pipe_dir(graph[ny][nx])])
                else:
                    if graph[y][x]=='M' or graph[y][x]=='Z':
                        continue
                    if fy==0 and fx==0:
                        fy, fx = ny, nx
                    if nd not in ans:
                        ans.append(nd)

r, c = map(int, input().split())
visited = [[False]*c for _ in range(r)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

graph = []
for i in range(r):
    graph.append(list(input().strip()))
    for j in range(c):
        if graph[i][j] == 'M':
            my, mx = i, j
        elif graph[i][j] == 'Z':
            zy, zx = i, j

ans, fy, fx = [], 0, 0

bfs(my, mx, [0, 1, 2, 3])
bfs(zy, zx, [0, 1, 2, 3])

for i in range(r):
    for j in range(c):
        if graph[i][j] != '.' and not visited[i][j]:
            bfs(i, j, pipe_dir(graph[i][j]))

ans.sort()

dir_lst = ['|', '-', '+', '1', '2', '3', '4']
for d in dir_lst:
    if ans == pipe_dir(d):
        print(fy+1, fx+1, d)