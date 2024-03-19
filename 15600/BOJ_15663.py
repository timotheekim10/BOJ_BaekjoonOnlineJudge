import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

array = []
visited = [False]*n

def backtracking():
    if len(array) == m:
        print(*array)
        return
    temp = 0
    for i in range(n):
        if temp != nums[i] and not visited[i]:
            visited[i] = True
            array.append(nums[i])
            temp = nums[i]
            backtracking()
            visited[i] = False
            array.pop()

backtracking()