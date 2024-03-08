import sys
from collections import deque

input = sys.stdin.readline

a, k = map(int, input().split())

dp = [0]*(k+1)

queue = deque()
queue.append(a)

while queue:
    x = queue.popleft()
    for i in range(2):
        if i == 0:
            nx = x+1
        else:
            nx = 2*x
        if 1<=nx<=k and dp[nx]==0:
            queue.append(nx)
            dp[nx] = dp[x]+1

print(dp[k])