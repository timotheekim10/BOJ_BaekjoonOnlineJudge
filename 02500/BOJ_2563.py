import sys

input = sys.stdin.readline

n = int(input())

graph = [[False] * 100 for _ in range(100)]

for _ in range(n):
    a, b = map(int, input().split())
    for i in range(a, a+10):
        for j in range(b, b+10):
            graph[i][j] = True

temp = 0

for i in range(100):
    for j in range(100):
        if not graph[i][j]:
            temp += 1

ans = 10000 - temp
print(ans)