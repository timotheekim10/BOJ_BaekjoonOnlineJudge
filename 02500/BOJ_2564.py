import sys

input = sys.stdin.readline

w, h = map(int, input().split())
n = int(input())
store = []

for _ in range(n):
    a, b = map(int, input().split())
    store.append((a, b))
x, y = map(int, input().split())

ans = 0

for s in store:
    a, b = s
    
    if x==1:
        if a==1: ans += abs(y-b)
        elif a==2: ans += h + min(y+b, (w-y)+(w-b))
        elif a==3: ans += y + b
        elif a==4: ans += (w-y) + b

    elif x==2:
        if a==1: ans += h + min(y+b, (w-y)+(w-b))
        elif a==2: ans += abs(y-b)
        elif a==3: ans += y + (h-b)
        elif a==4: ans += (w-y) + (h-b)

    elif x==3:
        if a==1: ans += y + b
        elif a==2: ans += (h-y) + b
        elif a==3: ans += abs(y-b)
        elif a==4: ans += w + min(y+b, (h-y)+(h-b))

    elif x==4:
        if a==1: ans += y + (w-b)
        elif a==2: ans += (h-y) + (w-b)
        elif a==3: ans += w + min(y+b, (h-y)+(h-b))
        elif a==4: ans += abs(y-b)

print(ans)