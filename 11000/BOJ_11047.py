import sys
input = sys.stdin.readline

cnt = 0
A = []

N, K = map(int, input().split())

for _ in range(N):
    A.append(int(input()))

A = A[::-1]

for coin in A:
    cnt += K//coin
    K %= coin

print(cnt)
