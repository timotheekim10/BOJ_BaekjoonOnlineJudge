import sys
input = sys.stdin.readline

A, B = [], []

N, M = map(int, input().split())
for _ in range(N):
    A.append(list(map(int, input().split())))

M, K = map(int, input().split())
for _ in range(M):
    B.append(list(map(int, input().split())))

C = [[0] * N for _ in range(K)]
for n in range(N):
    for k in range(K):
        sum = 0
        for m in range(M):
            sum += A[n][m] * B[m][k]
        print(sum, end=' ')
    print()