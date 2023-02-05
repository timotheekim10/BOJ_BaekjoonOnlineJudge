while True:
    word = input()
    if word[0] == '.' and len(word) == 1:
        break

    stack = []
    isVPS = True

    for item in word:
        if item in ('(', '['):
            stack.append(item)
        elif item in (')', ']'):
            if stack:
                if item == ')' and stack[-1] == '(':
                    stack.pop()
                elif item == ')' and stack[-1] == '[':
                    isVPS = False
                    break
                elif item == ']' and stack[-1] == '[':
                    stack.pop()
                elif item == ']' and stack[-1] == '(':
                    isVPS = False
                    break
            else:
                isVPS = False
                break

    if not stack and isVPS:
        print('yes')
    else:
        print('no')
