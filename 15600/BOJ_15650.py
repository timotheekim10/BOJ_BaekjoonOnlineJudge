import sys

input = sys.stdin.readline

n, m = list(map(int, input().split()))
 
array = []
temp = []
 
def backtracking():
    if len(array) == m:
        if list(set(array)) not in temp:
            print(*array)
            temp.append(list(set(array)))
        return
    
    for i in range(1, n+1):
        if i not in array:
            array.append(i)
            backtracking()
            array.pop()
 
backtracking()