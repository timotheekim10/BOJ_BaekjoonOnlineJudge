import sys
input = sys.stdin.readline

users = []

n = int(input())

for _ in range(n):
    age, name = map(str, input().split())
    age = int(age)
    users.append((age, name))

users.sort(key=lambda x:x[0])

for user in users:
    print(user[0], user[1])