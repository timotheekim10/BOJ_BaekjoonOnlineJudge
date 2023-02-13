from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
q = deque([i for i in range(1, N+1)])

print('<', end='')
while q:
    for _ in range(K-1):
        q.append(q.popleft())
    print(q.popleft(), end='')
    if q:
        print(', ', end='')
print('>')
