import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    q = deque()
    q.append((hx, hy))
    while q:
        x, y = q.popleft()
        if abs(fx - x) + abs(fy - y) <= 1000:
            print('happy')
            return
        for i in range(n):
            if not visited[i]:
                nx, ny = c[i]
                if abs(nx - x) + abs(ny - y) <= 1000:
                    visited[i] = True
                    q.append((nx, ny))
    print('sad')
    return

t = int(input())
for _ in range(t):
    n = int(input())
    hx, hy = map(int, input().split())
    c = []
    for _ in range(n):
        x, y = map(int, input().split())
        c.append((x, y))
    fx, fy = map(int, input().split())
    visited = [False] * n
    bfs()