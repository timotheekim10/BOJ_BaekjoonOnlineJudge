import sys

input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))

arr = []
ans = 0

def backtracking(start):
    global ans

    if sum(arr)==s and len(arr)>0:
        ans += 1
    
    for i in range(start, n):
        arr.append(nums[i])
        backtracking(i+1)
        arr.pop()

backtracking(0)
print(ans)