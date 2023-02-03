import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(n)]
prefixSum = [[0]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        prefixSum[i][j] = prefixSum[i][j-1] + \
            prefixSum[i-1][j] - prefixSum[i-1][j-1] + nums[i-1][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(prefixSum[x2][y2] - prefixSum[x2][y1-1] -
          prefixSum[x1-1][y2] + prefixSum[x1-1][y1-1])
