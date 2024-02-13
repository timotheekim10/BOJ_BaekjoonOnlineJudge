import sys

input = sys.stdin.readline

stack = []

n = int(input())

for _ in range(n):
    command = input().split()
    if int(command[0]) == 1:
        stack.append(int(command[1]))
    elif int(command[0]) == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif int(command[0]) == 3:
        print(len(stack))
    elif int(command[0]) == 4:
        if stack:
            print(0)
        else:
            print(1)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)