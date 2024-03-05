import sys

input = sys.stdin.readline

n, m, q = map(int, input().split())
array = [[0] * m] * n

for i in range(n):
    array[i] = list(map(int, input().split()))

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 0:
        array[query[1]][query[2]] = query[3]
    elif query[0] == 1:
        array[query[1]], array[query[2]] = array[query[2]], array[query[1]]

for i in range(n):
    row = map(str, array[i])
    print(" ".join(row))