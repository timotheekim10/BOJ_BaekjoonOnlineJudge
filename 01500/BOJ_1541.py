sub = input().split('-')
min_calc = []

for sub_num in sub:
    sum = 0
    add = sub_num.split('+')
    for add_num in add:
        sum += int(add_num)
    min_calc.append(sum)

for i in range(1, len(min_calc)):
    min_calc[0] -= min_calc[i]

print(min_calc[0])
