import sys
input = sys.stdin.readline

ascending = True
descending = True
mixed = True

nums = list(map(int, input().split()))
for i in range(1, 8):
    if nums[i-1] > nums[i]:
        ascending = False
    else:
        descending = False

if (ascending == False) and (descending == False):
    print('mixed')
elif ascending == True:
    print('ascending')
else:
    print('descending')
