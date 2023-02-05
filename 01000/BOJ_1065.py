cnt = 0

N = int(input())

for num in range(1, N+1):
    if num < 10:
        cnt += 1
    elif num < 100:
        cnt += 1
    else:
        strNum = str(num)
        if int(strNum[0])-int(strNum[1]) == int(strNum[1])-int(strNum[2]):
            cnt += 1

print(cnt)
