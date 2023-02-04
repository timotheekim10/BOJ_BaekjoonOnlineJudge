import sys
input = sys.stdin.readline

max = float('-inf')
min = float('+inf')

N = int(input())
nums = list(map(int, input().split()))

for num in nums:
    if num > max:
        max = num
    if num < min:
        min = num

print(min, max)
