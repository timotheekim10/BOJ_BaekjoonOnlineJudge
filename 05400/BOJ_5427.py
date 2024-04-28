import sys
from collections import deque

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(a, b):
    q = deque()
    visited = [[0] * w for _ in range(h)]
    q.append((a, b))
    visited[a][b] = 1

    for i in range(h):
        for j in range(w):
            if graph[i][j] == '*':
                visited[i][j] = -1
                q.append((i, j))
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx<0 or nx>=h or ny<0 or ny>=w:
                if visited[x][y] > 0:
                    return visited[x][y]
            elif 0<=nx<h and 0<=ny<w:
                if graph[nx][ny] == '.':
                    if visited[x][y] > 0 and not visited[nx][ny]:
                        visited[nx][ny] = visited[x][y] + 1
                        q.append((nx, ny))
                    elif visited[nx][ny] >= 0 and visited[x][y] == -1:
                        visited[nx][ny] = -1
                        q.append((nx,ny))
    return 'IMPOSSIBLE'

t = int(input())

for _ in range(t):
    w, h = map(int, input().split())
    graph = []
    for i in range(h):
        graph.append(list(map(str, input().strip())))
    for i in range(h):
        for j in range(w):
            if graph[i][j] == '@':
                print(bfs(i, j))
                break