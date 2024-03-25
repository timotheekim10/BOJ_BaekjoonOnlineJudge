import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]

parents = [0]*(n+1)
visited = [False]*(n+1)

for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque()
queue.append(1)
visited[1] = True

while queue:
    node = queue.popleft()
    for child in graph[node]:
        if not visited[child]:
            visited[child] = True
            parents[child] = node
            queue.append(child)

for i in range(2, n+1):
    print(parents[i])