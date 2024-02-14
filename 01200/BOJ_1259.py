while True:
    x = str(input())
    if x == '0':
        break
    is_palindrome = True
    for i in range(len(x)//2):
        if x[i] != x[-1-i]:
            is_palindrome = False
            break
    if is_palindrome:
        print('yes')
    else:
        print('no')