cnt = 0

N = int(input())

for _ in range(N):
    isGroup = True
    word = input()
    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            if word[i] in word[i+2:]:
                isGroup = False
                break
    if isGroup:
        cnt += 1

print(cnt)
