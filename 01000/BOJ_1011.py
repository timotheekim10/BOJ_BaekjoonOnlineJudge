import sys
import math

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    dist = y - x
    temp = math.ceil(math.sqrt(dist))
    cnt = temp*2-1
    if  temp**2-dist > cnt // 2:
        cnt -= 1
    print(cnt)