import sys

input = sys.stdin.readline

n, k = map(int, input().split())

arr = [0] * 7 * 2
ans = 0

for i in range(n):
    s, y = map(int, input().split())
    arr[2*y+s] += 1

for i in arr:
    ans += i//k
    if i%k: ans += 1

print(ans)