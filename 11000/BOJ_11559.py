import sys
from collections import deque

input = sys.stdin.readline

graph = [list(input().strip()) for _ in range(12)]
visited = [[False]*6 for _ in range(12)]
ans = 0

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def bfs(y, x):
    q = deque()
    q.append((y, x))
    visited[y][x] = True
    same = [(y, x)]

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<12 and 0<=nx<6 and graph[y][x]==graph[ny][nx] and not visited[ny][nx]:
                q.append((ny, nx))
                visited[ny][nx] = True
                same.append((ny, nx))
    return same

def delete(same):
    for y, x in same:
        graph[y][x] = '.'

def down():
    for x in range(6):
        for y in range(10, -1, -1):
            for k in range(11, y, -1):
                if graph[y][x]!='.' and graph[k][x]=='.':
                    graph[k][x] = graph[y][x]
                    graph[y][x] = '.'

while True:
    boom = False
    visited = [[False]*6 for _ in range(12)]
    for y in range(12):
        for x in range(6):
            if graph[y][x]!='.' and not visited[y][x]:
                same = bfs(y, x)
                if len(same) >= 4:
                    boom = True
                    delete(same)
    if boom:
        down()
        ans += 1
    else:
        break

print(ans)