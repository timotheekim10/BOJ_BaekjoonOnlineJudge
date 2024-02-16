import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

map = [list(map(int, input().strip())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
cnt_lst = []

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def bfs(a, b):
    queue = deque([[a, b]])
    visited[a][b] = 1
    cnt = 1
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0<=ny<n and 0<=nx<n and map[ny][nx]==1 and visited[ny][nx]==0:
                queue.append([ny, nx])
                visited[ny][nx] = 1
                cnt += 1
    return cnt

for i in range(n):
    for j in range(n):
        if map[i][j] == 1 and visited[i][j] == 0:
            cnt_lst.append(bfs(i, j))

cnt_lst.sort()

print(len(cnt_lst))

for cnt in cnt_lst:
    print(cnt)