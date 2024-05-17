import sys

n = int(input())

arr = []

for _ in range(n):
    l, h = map(int, input().split())
    arr.append([l, h])

arr.sort()

temp = 0
max_idx, max_height = 0, 0

for i in arr:
    if i[1] > max_height:
        max_height = i[1]
        max_idx = temp
    temp += 1

ans = max_height   

height = arr[0][1]

for i in range(max_idx):
    if height < arr[i+1][1]:
        ans += height * (arr[i+1][0] - arr[i][0])
        height = arr[i+1][1]
    else:
        ans += height * (arr[i+1][0] - arr[i][0])
    
height = arr[-1][1]

for i in range(n-1, max_idx, -1):
    if height < arr[i-1][1]:
        ans += height * (arr[i][0] - arr[i-1][0])
        height = arr[i-1][1]
    else:
        ans += height * (arr[i][0] - arr[i-1][0])

print(ans)