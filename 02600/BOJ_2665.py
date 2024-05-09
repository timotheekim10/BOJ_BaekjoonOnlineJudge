import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


q = deque()
q.append((0, 0))
visited = [[-1] * n for _ in range(n)]
visited[0][0] = 0

while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0<=nx<n and 0<=ny<n and visited[nx][ny]==-1:
            if graph[nx][ny] == 1:
                q.appendleft((nx, ny))
                visited[nx][ny] = visited[x][y]
            else:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                
            if nx==n-1 and ny==n-1:
                print(visited[nx][ny])
                sys.exit(0)