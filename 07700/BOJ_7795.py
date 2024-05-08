import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()
    a_idx, b_idx, temp, cnt = 0, 0, 0, 0

    while a_idx < n:
        if b_idx >= m:
            a_idx += 1
            cnt += temp
            continue

        if a[a_idx] > b[b_idx]:
            b_idx += 1
            temp += 1
        else:
            a_idx += 1
            cnt += temp
            
    print(cnt)