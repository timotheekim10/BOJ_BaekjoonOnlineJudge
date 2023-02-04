import sys
input = sys.stdin.readline

score = 0
bonus = 1

n = int(input())
for _ in range(n):
    quizAnswers = input()
    for answer in quizAnswers:
        if answer == 'O':
            score += bonus
            bonus += 1
        else:
            bonus = 1
    print(score)
    score, bonus = 0, 1
