import sys

input = sys.stdin.readline

w, h = map(int, input().split())
n = int(input())

w_lst = [False] * (w+1)
h_lst = [False] * (h+1)

for _ in range(n):
    a, b = map(int, input().split())
    if a==0: h_lst[b] = True
    elif a==1: w_lst[b] = True

temp_w = -1
ans_w = []

for i in range(w+1):
    if not w_lst[i]:
        temp_w += 1
        if i==w:
            ans_w.append(temp_w)
    else:
        ans_w.append(temp_w + 1)
        temp_w = 0

temp_h = -1
ans_h = []

for i in range(h+1):
    if not h_lst[i]:
        temp_h += 1
        if i==h:
            ans_h.append(temp_h)
    else:
        ans_h.append(temp_h + 1)
        temp_h = 0

print(max(ans_w) * max(ans_h))