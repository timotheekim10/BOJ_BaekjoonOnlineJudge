import sys

from collections import deque

input = sys.stdin.readline

graph = [list(map(int, input().split())) for _ in range(5)]
visited = [[0]*5 for _ in range(5)]
start = list(map(int, input().split()))

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

queue = deque([])
queue.append(start)

while queue:
    y, x = queue.popleft()
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0<=ny<5 and 0<=nx<5 and graph[ny][nx]!=-1 and visited[ny][nx]==0:
            visited[ny][nx] = visited[y][x] + 1
            if graph[ny][nx] == 1:
                print(visited[ny][nx])
                sys.exit(0)
            queue.append([ny, nx])

print(-1)