import sys

input = sys.stdin.readline

n = int(input())

array = [list(map(int, input().split())) for _ in range(n)]

array.sort(key=lambda x: x[0])
mid_x = array[n//2][0]
array.sort(key=lambda x: x[1])
mid_y = array[n//2][1]

manhattan_distance = 0

for i in range(n):
    manhattan_distance += (abs(mid_x-array[i][0]) + abs(mid_y-array[i][1]))

print(manhattan_distance)