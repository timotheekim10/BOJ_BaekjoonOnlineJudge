import sys
input = sys.stdin.readline

sum = 0

X = int(input())
N = int(input())

for _ in range(N):
    a, b = map(int, input().split())
    sum += a*b

if X == sum:
    print('Yes')
else:
    print('No')
