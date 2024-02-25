import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [0] * 101
ladder, snake = dict(), dict()

for _ in range(n):
    i, j = map(int, input().split())
    ladder[i] = j

for _ in range(m):
    i, j = map(int, input().split())
    snake[i] = j

queue = deque([1])

while queue:
    px = queue.popleft()
    for i in range(1, 7):
        nx = px + i
        if 1<nx<=100 and graph[nx]==0:
            if nx in ladder:
                nx = ladder[nx]
            if nx in snake:
                nx = snake[nx]
            if graph[nx] == 0:
                queue.append(nx)
                graph[nx] = graph[px] + 1

print(graph[-1])