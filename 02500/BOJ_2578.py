import sys

input = sys.stdin.readline

def bingoCheck():
    cnt, temp = 0, 0
    for i in range(5):
        for j in range(5):
            if visited[i][j]:
                temp += 1
        if temp == 5:
            cnt += 1
        temp = 0
    
    for i in range(5):
        for j in range(5):
            if visited[j][i]:
                temp += 1
        if temp == 5:
            cnt += 1
        temp = 0

    for i in range(5):
        if visited[i][i]:
            temp += 1
    if temp == 5:
        cnt += 1
    temp = 0

    for i in range(5):
        if visited[i][4-i]:
            temp += 1
    if temp == 5:
        cnt += 1

    if cnt >= 3:
        return True
    else:
        return False

board = [list(map(int, input().split())) for _ in range(5)]

array = []

for _ in range(5):
    array += list(map(int, input().split()))

visited = [[False] * 5 for _ in range(5)]
ans = 1

for i in array:
    for j in range(5):
        for k in range(5):
            if board[j][k] == i:
                visited[j][k] = True
                if ans < 5:
                    ans += 1
                    continue
                if bingoCheck():
                    print(ans)
                    sys.exit(0)
                ans += 1