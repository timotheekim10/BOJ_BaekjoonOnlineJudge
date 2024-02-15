sum = 0

n = (input())

if '0' in n:
    for i in range(len(n)):
        sum += int(n[i])
    if sum%3 == 0:
        n = ''.join(sorted(n, reverse=True))
        print(n)
    else:
        print(-1)
else:
    print(-1)