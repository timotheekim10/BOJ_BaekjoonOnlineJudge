import sys
import heapq

input = sys.stdin.readline

m, n = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]
dist = [[1e10] * m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

heap = []
heapq.heappush(heap, (0, 0, 0))
dist[0][0] = 0

while heap:
    cost, x, y = heapq.heappop(heap)
    if cost > dist[x][y]:
        continue
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m:
            if cost + graph[nx][ny] < dist[nx][ny]:
                dist[nx][ny] = cost + graph[nx][ny]
                heapq.heappush(heap, (dist[nx][ny], nx, ny))

print(dist[n-1][m-1])