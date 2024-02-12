import sys
input = sys.stdin.readline

stack = []
sum = 0

k = int(input())

for _ in range(k):
    num = int(input())
    if num == 0:
        sum -= stack[-1]
        stack.pop()
    else:
        sum += num
        stack.append(num)

print(sum)