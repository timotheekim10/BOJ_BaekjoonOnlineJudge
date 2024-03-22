import sys
from collections import deque

input = sys.stdin.readline

row, column = map(int, input().split())
graph = [list(input()) for _ in range(row)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def bfs(start):
    dp = [[-1]*column for _ in range(row)]
    dp[start[0]][start[1]] = 0
    cnt = 0

    queue = deque([])
    queue.append(start)

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<row and 0<=nx<column and graph[ny][nx]=='L' and dp[ny][nx]==-1:
                dp[ny][nx] = dp[y][x] + 1
                cnt = max(cnt, dp[ny][nx])
                queue.append([ny, nx])

    return cnt

result = 0

for i in range(row):
    for j in range(column):
        if graph[i][j] == 'L':
            if 0<=i-1<row-2 and 2<=i+1<row:
                if graph[i-1][j]=='L' and graph[i+1][j]=='L':
                    continue
            if 0<=j-1<column-2 and 2<=i+1<column:
                if graph[i][j-1]=='L' and graph[i][j+1]=='L':
                    continue
            result = max(result, bfs([i, j]))

print(result)