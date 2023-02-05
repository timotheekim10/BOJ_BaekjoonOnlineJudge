time = 0

word = input()

for ch in word:
    if ord(ch) < 68:
        time += 3
    elif ord(ch) < 71:
        time += 4
    elif ord(ch) < 74:
        time += 5
    elif ord(ch) < 77:
        time += 6
    elif ord(ch) < 80:
        time += 7
    elif ord(ch) < 84:
        time += 8
    elif ord(ch) < 87:
        time += 9
    elif ord(ch) < 91:
        time += 10
    else:
        time += 11

print(time)
