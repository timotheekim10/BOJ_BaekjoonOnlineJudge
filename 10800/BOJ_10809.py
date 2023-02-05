S = input()
for i in range(26):
    try:
        print(S.index(chr(97+i)), end=' ')
    except:
        print('-1', end=' ')
