def gcd(a, b):
    while a*b != 0:
        if a > b:
            a = a%b
        else:
            b = b%a
    return a+b

def lcm(a, b):
    return a*b / gcd(a, b)

a, b = map(int, input().split())
print(int(lcm(a, b)))