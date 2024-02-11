cnt = 0

n = int(input())

for num in range(1, n+1):
    if num < 10:
        cnt += 1
    elif num < 100:
        cnt += 1
    else:
        str_num = str(num)
        if int(str_num[0])-int(str_num[1]) == int(str_num[1])-int(str_num[2]):
            cnt += 1

print(cnt)