T = int(input())

for i in range(T):
    stack = []
    isVPS = True
    ps = input()

    for item in ps:
        if item == '(':
            stack.append(item)
        else:
            if stack:
                stack.pop()
            else:
                isVPS = False
                break

    if not stack and isVPS:
        print('YES')
    else:
        print('NO')
