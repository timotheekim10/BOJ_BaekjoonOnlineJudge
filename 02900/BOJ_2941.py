croatiaAlphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

words = input()

for i in croatiaAlphabet:
    words = words.replace(i, '*')

print(len(words))
