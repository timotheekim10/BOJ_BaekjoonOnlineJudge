import sys
from collections import deque

input = sys.stdin.readline

dx = ['D', 'S', 'L', 'R']

def bfs(a, b):
    visited = ['.']*10000
    q = deque()
    q.append((a))
    visited[a] = ''
    while q:
        x = q.popleft()
        for i in dx:
            if i=='D':
                nx = x*2 % 10000
            elif i=='S':
                nx = x - 1 if x != 0 else 9999
            elif i=='L':
                nx = (x%1000)*10 + x//1000
            elif i=='R':
                nx = (x%10)*1000 + x//10
            if 0<=nx<10000 and visited[nx] == '.':
                q.append(nx)
                visited[nx] = visited[x] + i
                if nx == b:
                    print(visited[nx])
                    return

t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    bfs(a, b)