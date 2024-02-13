import sys

input = sys.stdin.readline

h_lst, stack = [], []
sum, cnt = 0, -1

n = int(input())

for _ in range(n):
    h_lst.append(int(input()))

for h in h_lst:
    while stack and h >= stack[-1]:
        stack.pop()
        cnt -= 1
    stack.append(h)
    cnt += 1
    sum += cnt
print(sum)