import sys
from collections import deque
from itertools import permutations

input = sys.stdin.readline

n = int(input())
scv = list(map(int, input().split()))

scv += [0]*(3-n)
dp = [[[-1]*61 for _ in range(61)] for _ in range(61)]
dp[scv[0]][scv[1]][scv[2]] = 0

queue = deque()
queue.append([scv[0], scv[1], scv[2]])
    
while queue:
    hp = queue.popleft()

    if hp[0]==0 and hp[1]==0 and hp[2]==0:
        print(dp[hp[0]][hp[1]][hp[2]])
        break

    for case in permutations([9, 3, 1], 3):
        new_hp = [max(hp[0]-case[0], 0), max(hp[1]-case[1], 0), max(hp[2]-case[2], 0)]

        if dp[new_hp[0]][new_hp[1]][new_hp[2]] == -1:
            dp[new_hp[0]][new_hp[1]][new_hp[2]] = dp[hp[0]][hp[1]][hp[2]] + 1
            queue.append(new_hp)