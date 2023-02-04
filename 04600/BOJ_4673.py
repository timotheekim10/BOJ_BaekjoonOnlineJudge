def notSelfNum(n):
    if n < 10:
        notSelfNums.append(n+n)
    elif n < 100:
        notSelfNums.append(n+n//10+n % 10)
    elif n < 1000:
        notSelfNums.append(n+n//100+n//10 % 10+n % 10)
    elif n < 10000:
        notSelfNums.append(n+n//1000+n//100 % 10+n//10 % 10+n % 10)


nums = [num for num in range(1, 10001)]
notSelfNums = []

for i in range(1, 10000):
    notSelfNum(i)

selfNums = sorted(list(set(nums)-set(notSelfNums)))
for selfNum in selfNums:
    print(selfNum)
