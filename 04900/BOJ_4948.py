import sys
import math

input = sys.stdin.readline

prime_num = [1 for _ in range(123456*2+1)]
prime_num[0], prime_num[1] = 0, 0

for i in range(2, 123456*2+1):
    for j in range(2, int(math.sqrt(i))+1):
        if i%j == 0:
            prime_num[i] = 0
            break

while True:
    n = int(input())
    if n == 0:
        break
    cnt = 0
    for i in range(n+1, 2*n+1):
        if prime_num[i] == 1:
            cnt += 1
    print(cnt)