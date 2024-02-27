import sys

input = sys.stdin.readline

n, m = map(int, input().split())

DNAs = []

for _ in range(n):
    DNAs.append(input())
        
answer, cnt = '', 0

for i in range(m):
    DNA_dict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for j in range(n):
        if DNAs[j][i] == 'A':
            DNA_dict['A'] += 1
        elif DNAs[j][i] == 'C':
            DNA_dict['C'] += 1
        elif DNAs[j][i] == 'G':
             DNA_dict['G'] += 1
        elif DNAs[j][i] == 'T':
            DNA_dict['T'] += 1
    key = max(DNA_dict, key=DNA_dict.get)
    if key == 'A':
        answer += 'A'
    elif key == 'C':
        answer += 'C'
    elif key == 'G':
         answer += 'G'
    elif key == 'T':
        answer += 'T'
    cnt += n - max(DNA_dict.values())

print(answer)
print(cnt)