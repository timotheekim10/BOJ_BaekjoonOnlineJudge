import sys
input = sys.stdin.readline

stack = []
sum = 0

k = int(input())

for _ in range(k):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

if len(stack) == 0:
    print(0)
else:
    for num in stack:
        sum += num
    print(sum)
