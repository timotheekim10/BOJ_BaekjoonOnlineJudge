import sys

n = int(input())

ans = []

for y in range(n+1):
    x = n
    arr = [n]
    cnt = 1
    while y >= 0:
        arr.append(y)
        cnt += 1
        x, y = y, x-y
    arr.append(cnt)
    ans.append(arr)

ans.sort(key= lambda x : -x[-1])

print(ans[0][-1])
ans_arr = ans[0][:-1]
print(*ans_arr)