import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

array = [0]
visited = [False] * (n+1)

def backtracking():
    if len(array) == m+1:
        ans = array[1:]
        print(*ans)
        return
    temp = 0
    for i in range(1, n+1):
        if temp != nums[i-1] and array[-1] <= nums[i-1] and not visited[i]:
            visited[i] = True
            array.append(nums[i-1])
            temp = nums[i-1]
            backtracking()
            visited[i] = False
            array.pop()

backtracking()