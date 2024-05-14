import sys

input = sys.stdin.readline

k = int(input())

arr = []
w_lst, h_lst = [], []

for _ in range(6):
    x, y = map(int, input().split())

    arr.append((x, y))

    if x == 3 or x == 4: w_lst.append(y)
    elif x == 1 or x == 2: h_lst.append(y)

w = max(w_lst)
h = max(h_lst)

for i in range(6):
    if i == 0:
        if arr[i][0] == 1:
            if arr[5][0] == 3:
                continue
            else:
                print(k * ((w * h) - (arr[i][1] * arr[5][1])))
                sys.exit(0)
        elif arr[i][0] == 2:
            if arr[5][0] == 4:
                continue
            else:
                print(k * ((w * h) - (arr[i][1] * arr[5][1])))
                sys.exit(0)
        elif arr[i][0] == 3:
            if arr[5][0] == 2:
                continue
            else:
                print(k * ((w * h) - (arr[i][1] * arr[5][1])))
                sys.exit(0)
        elif arr[i][0] == 4:
            if arr[5][0] == 1:
                continue
            else:
                print(k * ((w * h) - (arr[i][1] * arr[5][1])))
                sys.exit(0)
    else:
        if arr[i][0] == 1:
            if arr[i-1][0] == 3:
                continue
            else:
                print(k * ((w * h) - (arr[i][1] * arr[i-1][1])))
                sys.exit(0)
        elif arr[i][0] == 2:
            if arr[i-1][0] == 4:
                continue
            else:
                print(k * ((w * h) - (arr[i][1] * arr[i-1][1])))
                sys.exit(0)
        elif arr[i][0] == 3:
            if arr[i-1][0] == 2:
                continue
            else:
                print(k * ((w * h) - (arr[i][1] * arr[i-1][1])))
                sys.exit(0)
        elif arr[i][0] == 4:
            if arr[i-1][0] == 1:
                continue
            else:
                print(k * ((w * h) - (arr[i][1] * arr[i-1][1])))
                sys.exit(0)