import sys
input = sys.stdin.readline

stack = []

N = int(input())

for _ in range(N):
    words = input().split()

    if words[0] == 'push':
        value = words[1]
        stack.append(value)

    elif words[0] == 'pop':
        if len(stack) == 0:
            print('-1')
        else:
            print(stack.pop())

    elif words[0] == 'size':
        print(len(stack))

    elif words[0] == 'empty':
        if len(stack) == 0:
            print('1')
        else:
            print('0')

    elif words[0] == 'top':
        if len(stack) == 0:
            print('-1')
        else:
            print(stack[-1])
