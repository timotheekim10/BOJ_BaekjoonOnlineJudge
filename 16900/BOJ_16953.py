import sys
from collections import deque

input = sys.stdin.readline

a, b = map(int, input().split())

queue = deque([])
queue.append((a, 1))

while queue:
    x, count = queue.popleft()

    if x == b:
        print(count)
        sys.exit(0)

    for i in range(2):
        if i == 0:
            nx = 2*x
        else:
            nx = 10*x + 1
        if nx <= b:
            queue.append((nx, count+1))

print(-1)