import sys

input = sys.stdin.readline

s = input()

q = int(input())

prefix_sum = []

for i in range(ord('a'), ord('z')+1):
    temp = [0]
    sum = 0
    for j in s:
        if ord(j) == i:
            sum += 1
        temp.append(sum)
    prefix_sum.append(temp)
            
for _ in range(q):
    a, l, r = map(str, input().split())
    print(prefix_sum[ord(a)-ord('a')][int(r)+1]-prefix_sum[ord(a)-ord('a')][int(l)])