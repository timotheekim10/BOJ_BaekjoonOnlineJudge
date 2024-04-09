import sys
from collections import deque

input = sys.stdin.readline

f, s, g, u, d = map(int, input().split())

if s == g:
    print(0)
    sys.exit(0)

graph = [-1] * (f+1)

dx = [u, -d]

q = deque()
q.append(s)
graph[s] = 0

while q:
    x = q.popleft()
    for i in dx:
        nx = x + i
        if 0<nx<=f and graph[nx]==-1:
            graph[nx] = graph[x] + 1
            if nx==g:
                print(graph[nx])
                sys.exit(0)
            q.append(nx)

print('use the stairs')