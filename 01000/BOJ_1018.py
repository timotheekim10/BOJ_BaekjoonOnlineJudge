import sys

input = sys.stdin.readline

chess, cnt_lst = [], []

n, m = map(int, input().split())

for _ in range(n):
    chess.append(input())

for i in range(n-7):
    for j in range(m-7):
        cnt = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l)%2 == 0:
                    color = 'W'
                else:
                    color = 'B'
                if chess[k][l] != color:
                    cnt += 1
        if cnt > 32:
            cnt = 64 - cnt
        cnt_lst.append(cnt)

print(min(cnt_lst))
