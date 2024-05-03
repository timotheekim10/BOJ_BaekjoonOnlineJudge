import sys

input = sys.stdin.readline

n, m = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()

array = []

def backtracking():
    if len(array) == m:
        print(*array)
        return
    temp = 0
    for i in range(n):
        if temp != nums[i]:
            array.append(nums[i])
            temp = nums[i]
            backtracking()
            array.pop()

backtracking()