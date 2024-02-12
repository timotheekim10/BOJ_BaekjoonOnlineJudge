import sys
input = sys.stdin.readline

people = []

n = int(input())

for _ in range(n):
    person = list(map(int, input().split()))
    people.append(person)

for i in range(len(people)):
    order = 1
    for j in range(len(people)):
        if i == j:
            continue
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            order += 1
    print(order, end = ' ')