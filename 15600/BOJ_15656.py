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
    
    for i in range(n):
        array.append(nums[i])
        backtracking()
        array.pop()

backtracking()