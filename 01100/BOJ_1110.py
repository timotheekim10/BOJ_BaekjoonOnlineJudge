cycle = 0

N = int(input())
temp = N

while True:
    cycle += 1
    temp = temp % 10*10 + (temp//10+temp % 10) % 10
    if temp == N:
        print(cycle)
        break
