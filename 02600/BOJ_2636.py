import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    visited = [[False] * m for _ in range(n)]
    q = deque()
    q.append((0, 0))
    cnt = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                elif graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    graph[nx][ny] = 0
                    cnt += 1
    return cnt

time, ans_cnt = 0, 0

while True:
    temp = True
    ans_cnt = bfs()
    time += 1
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                temp = False
    if temp:
        break

print(time)
print(ans_cnt)