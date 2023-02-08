import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))

P = sorted(P)
temp = 0
min_time = 0
for person_time in P:
    temp += person_time
    min_time += temp
print(min_time)
