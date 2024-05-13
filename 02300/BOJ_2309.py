import sys

input = sys.stdin.readline

height = []

for _ in range(9):
    height.append(int(input()))

arr = []

def backtracking():
    if len(arr) == 7:
        if sum(arr) == 100:
            arr.sort()
            print(*arr, sep='\n')
            sys.exit(0)
        return
    
    for h in height:
        if h not in arr:
            arr.append(h)
            backtracking()
            arr.pop()

backtracking()       