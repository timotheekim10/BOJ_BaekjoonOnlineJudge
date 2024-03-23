import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(n-1):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))

def bfs(start, end):
    visited = [False]*(n + 1)
    queue = deque([(start, 0)])
    visited[start] = True

    while queue:
        node, distance = queue.popleft()
        if node == end:
            return distance

        for neighbor, edge_length in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, distance+edge_length))

results = []

for _ in range(m):
    a, b = map(int, input().split())
    results.append(bfs(a, b))

for result in results:
    print(result)