import sys
input = sys.stdin.readline

C = int(input())

for _ in range(C):
    scores = list(map(int, input().split()))
    avg = sum(scores[1:])/scores[0]
    count = 0
    for score in scores[1:]:
        if score > avg:
            count += 1
    rate = count/scores[0]*100
    print(f'{rate:.3f}%')
