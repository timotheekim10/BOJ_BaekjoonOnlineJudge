import sys
import math

input = sys.stdin.readline

m, n = map(int, input().split())

for i in range(m, n+1):
    is_prime = True
    if i == 1:
        is_prime = False
    for j in range(2, int(math.sqrt(i))+1):
        if i%j == 0:
            is_prime = False
            break
    if is_prime:
        print(i)
