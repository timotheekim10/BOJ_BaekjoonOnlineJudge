import sys
input = sys.stdin.readline

M = float('-inf')
sum = 0

N = int(input())
scores = list(map(int, input().split()))

for score in scores:
    if score > M:
        M = score

for i in range(N):
    scores[i] = scores[i] / M * 100
    sum += scores[i]

print(sum/N)
