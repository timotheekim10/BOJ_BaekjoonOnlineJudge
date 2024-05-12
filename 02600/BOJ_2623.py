import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
temp = [0] * (n+1)

for i in range(m):
    lst = list(map(int, input().split()))
    idx = 1
    while idx <= lst[0]-1:
        if lst[idx+1] not in graph[lst[idx]]:
            graph[lst[idx]].append(lst[idx+1])
            temp[lst[idx+1]] += 1
        idx += 1

q = deque()

for s in range(1, n+1):
    if temp[s] == 0:
        q.append(s)

ans = []

while q:
    s = q.popleft()
    ans.append(s)
    for adj_s in graph[s]:
        temp[adj_s] -= 1
        if temp[adj_s] == 0:
            q.append(adj_s)

if len(ans) == n:
    print(*ans)
else:
    print(0)