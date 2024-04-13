import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())

graph, house, chicken = [], [], []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] == 1:
            house.append((i, j))
        elif graph[i][j] == 2:
            chicken.append((i, j))

ans = 1e9

for c in list(combinations(chicken, m)):
    total_d = 0
    for h in house:
        d = 100
        for i in range(m):
            d = min(d, abs(h[0] - c[i][0]) + abs(h[1] - c[i][1]))
        total_d += d
    ans = min(ans, total_d)

print(ans)