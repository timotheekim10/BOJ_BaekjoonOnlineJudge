import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[0]*(n+1) for _ in range(n+1)]
dfs_visited, bfs_visited = [0]*(n+1), [0]*(n+1)

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1][v2] = graph[v2][v1] = 1

def dfs(v):
    print(v, end=' ')
    dfs_visited[v] = 1
    for i in range(1, n+1):
        if graph[v][i] == 1 and dfs_visited[i] == 0:
            dfs(i)

def bfs(v):
    queue = deque([v])
    bfs_visited[v] = 1
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in range(1, n+1):
            if graph[v][i] == 1 and bfs_visited[i] == 0:
                queue.append(i)
                bfs_visited[i] = 1

dfs(v)
print()
bfs(v)