import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

maze = [list(map(int, input().strip())) for _ in range(n)]
visited, dp = [[0]*m for _ in range(n)], [[0]*m for _ in range(n)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

queue = deque([[0, 0]])
visited[0][0], dp[0][0] = 1, 1

while queue:
    y, x = queue.popleft()
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0<=ny<n and 0<=nx<m and maze[ny][nx]==1 and visited[ny][nx]==0:
            queue.append([ny, nx])
            visited[ny][nx] = 1
            dp[ny][nx] = dp[y][x] + 1

print(dp[n-1][m-1])