import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int,input().split())

max_size = 100001

queue = deque()
queue.append(n)

graph = [-1] * max_size
graph[n], cnt = 0, 0

while queue:
    x = queue.popleft()
    if x == k:
        cnt += 1
    for nx in [x*2, x+1, x-1]:
        if 0 <= nx < max_size:
            if graph[nx]==-1 or graph[nx]==graph[x]+1:
                graph[nx] = graph[x] + 1
                queue.append(nx)
 
print(graph[k])
print(cnt)