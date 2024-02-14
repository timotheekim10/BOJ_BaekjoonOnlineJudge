import sys

input = sys.stdin.readline

chess, cnt_lst = [], []

n, m = map(int, input().split())

for _ in range(n):
    chess.append(input())

for i in range(n-7):
    for j in range(m-7):
        order, cnt = 0, 0
        temp = True
        for k in range(i, i+8):
            for l in range(j, j+8):
                if order%8 == 0:
                    temp = temp
                else:
                    temp = not temp
                if temp:
                    color = 'W'
                else:
                    color = 'B'
                if chess[k][l] != color:
                    cnt += 1
                order += 1
        if cnt > 32:
            cnt = 64 - cnt
        cnt_lst.append(cnt)

print(min(cnt_lst))
