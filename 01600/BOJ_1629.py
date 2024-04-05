import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())

def power_mod(a, b):
    if b==1:
        return a%c

    temp = power_mod(a, b//2)

    if b%2:
        return temp*temp*a%c
    else:
        return temp*temp%c
        
print(power_mod(a, b))