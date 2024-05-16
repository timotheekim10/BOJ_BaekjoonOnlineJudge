import sys

input = sys.stdin.readline

for _ in range(4):
    x1, y1, x2, y2, p1, q1, p2, q2 = map(int, input().split())
    if x1>p2 or x2<p1 or y1>q2 or y2<q1:
        print('d')
    elif (x1==p2 and y1==q2) or (x1==p2 and y2==q1) or (x2==p1 and y2==q1) or (x2==p1 and y1==q2):
        print('c')
    elif x1==p2 or x2==p1 or y1==q2 or y2==q1:
        print('b')
    else:
        print('a')