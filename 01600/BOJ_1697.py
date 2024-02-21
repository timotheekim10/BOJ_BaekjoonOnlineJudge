import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

if n == k:
    print(0)
    sys.exit(0)

max_size = 100000

graph = [0] * (max_size + 1)

queue = deque()

graph[n] = 0
queue.append(n)

while queue:
    x = queue.popleft()
    for i in range(3):
        if i == 0:
            dx = 2*x
            if dx == 0:
                continue
        elif i == 1:
            dx = x+1
        else:
            dx = x-1
        if 0<=dx<=max_size and graph[dx] == 0:
            graph[dx] = graph[x] + 1
            queue.append(dx)
            if dx == k:
                print(graph[dx])
                sys.exit(0)