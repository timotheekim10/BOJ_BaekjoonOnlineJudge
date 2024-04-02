import sys

input = sys.stdin.readline

n = int(input())

ans = 0

for _ in range(n):
    a, b = map(int, input().split())
    temp = ans%(a+b)
    if b > temp:
        ans += b-temp
    ans+=1

print(ans)