import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
prefixSum = [[0]*(M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        prefixSum[i][j] = prefixSum[i][j-1] + \
            prefixSum[i-1][j] - prefixSum[i-1][j-1] + matrix[i-1][j-1]

K = int(input())
for _ in range(K):
    i, j, x, y = map(int, input().split())
    print(prefixSum[x][y]-prefixSum[x][j-1] -
          prefixSum[i-1][y]+prefixSum[i-1][j-1])
