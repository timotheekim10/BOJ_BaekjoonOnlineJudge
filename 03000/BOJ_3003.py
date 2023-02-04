import sys
input = sys.stdin.readline

chessPieces = [1, 1, 2, 2, 2, 8]

nums = list(map(int, input().split()))

for i in range(6):
    print(chessPieces[i] - nums[i], end=' ')
