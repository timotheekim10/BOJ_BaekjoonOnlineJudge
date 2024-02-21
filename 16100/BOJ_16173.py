import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph =[list(map(int, input().split())) for _ in range(n)]
visited = [['X']*n for _ in range(n)]

queue = deque([])
queue.append([0, 0])

while queue:
    y, x = queue.popleft()
    visited[y][x] = 'O'
    dy = [graph[y][x], 0]
    dx = [0, graph[y][x]]
    for i in range(2):
        ny, nx = y + dy[i], x + dx[i]
        if 0<=ny<n and 0<=nx<n and visited[ny][nx]=='X':
            if ny==n-1 and nx==n-1:
                print('HaruHaru')
                sys.exit(0)
            queue.append([ny, nx])
            visited[ny][nx] = 'O'

print('Hing')