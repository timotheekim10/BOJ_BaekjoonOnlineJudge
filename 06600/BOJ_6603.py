import sys

input = sys.stdin.readline

def backtracking(idx):
    if len(arr) == 6:
        print(*arr)
        return
    for i in range(idx, k):
        arr.append(s[i])
        backtracking(i+1)
        arr.pop()

while True:
    lst = list(map(int, input().split()))
    k = lst[0]
    s = lst[1:]
    if k == 0:
        sys.exit(0)
    arr = []
    backtracking(0)
    print()