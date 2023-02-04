max, order, maxOrder = float('-inf'), 1, 1

for _ in range(9):
    num = int(input())
    if num > max:
        max = num
        maxOrder = order
    order += 1

print(max)
print(maxOrder)
