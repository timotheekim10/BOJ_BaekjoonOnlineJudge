def notSelfNum(n):
    total = n
    while n != 0:
        total += n%10
        n //= 10
    return total

nums = [num for num in range(1, 10001)]
notSelfNums = []

for i in range(1, 10000):
    notSelfNums.append(notSelfNum(i))

selfNums = sorted(list(set(nums)-set(notSelfNums)))
for selfNum in selfNums:
    print(selfNum)