import sys
input = sys.stdin.readline

T = int(input())
for i in range(1, T+1):
    A, B = map(int, input().split())
    print('Case #{}: {} + {} = {}'.format(i, A, B, A+B))
