import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())

words = []

for _ in range(n):
  words.append(input().strip())

dict = defaultdict(int)

for word in words:
  for j in range(len(word)):
    dict[word[j]] += 10 ** (len(word)-1-j)

answer, temp = 0, 9

dict = sorted(dict.values(), reverse=True)

for i in dict:
  answer += i * temp
  temp -= 1

print(answer)