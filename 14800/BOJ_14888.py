import sys

input = sys.stdin.readline

n = int(input())
a_lst = list(map(int, input().split()))
op_lst = list(map(int, input().split()))

max_value, min_value = -1e9, 1e9

def backtracking(i, total, add, sub, mul, div):
    global max_value, min_value

    if i == n:
        max_value, min_value = max(total, max_value), min(total, min_value)
        return

    if add:
        backtracking(i+1, total+a_lst[i], add-1, sub, mul, div)
    if sub:
        backtracking(i+1, total-a_lst[i], add, sub-1, mul, div)
    if mul:
        backtracking(i+1, total*a_lst[i], add, sub, mul-1, div)
    if div:
        backtracking(i+1, int(total/a_lst[i]), add, sub, mul, div-1)

backtracking(1, a_lst[0], op_lst[0], op_lst[1], op_lst[2], op_lst[3])

print(max_value)
print(min_value)