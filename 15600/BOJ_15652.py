import sys

input = sys.stdin.readline

n, m = map(int, input().split())

array = [0]

def backtracking():
    if len(array) == m+1:
        temp = array[1:]
        print(*temp)
        return
    
    for i in range(1, n+1):
        if array[-1] <= i:
            array.append(i)
            backtracking()
            array.pop()

backtracking()