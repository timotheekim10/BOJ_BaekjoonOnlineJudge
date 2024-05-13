import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

ans = []
num = 1

for i in range(n):
    ans.insert(i-arr[i], num)
    num += 1

print(*ans)