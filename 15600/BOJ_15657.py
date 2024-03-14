import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

array = [0]

def backtracking():
    if len(array) == m+1:
        temp = array[1:]
        print(*temp)
        return
    
    for i in range(n):
        if array[-1] <= nums[i]:
            array.append(nums[i])
            backtracking()
            array.pop()

backtracking()