import sys
from collections import deque

input = sys.stdin.readline

gear = [deque(list(map(int,input().rstrip()))) for _ in range(4)]

k = int(input())
for _ in range(k):
	intersection = []
	for i in range(4):
		intersection.append([gear[i][6], gear[i][2]])
	gear_num, direction = map(int,input().split())
	gear_num -= 1
	if gear_num != 0 :
		for i in range(gear_num, 0, -1):
			if intersection[i][0] != intersection[i-1][1]:
				if (gear_num-(i-1))%2 == 0:
					gear[i-1].rotate(direction)
				elif (gear_num-(i-1))%2 != 0:
					gear[i-1].rotate(-1*direction)
			elif intersection[i][0] == intersection[i-1][1]:
				break          
	if gear_num != 3:
		for i in range(gear_num, 3):
			if intersection[i][1] != intersection[i+1][0]:
				if (gear_num-(i+1))%2 == 0:
					gear[i+1].rotate(direction)
				elif (gear_num-(i+1))%2 != 0:
					gear[i+1].rotate(-1*direction)
			elif intersection[i][1] == intersection[i+1][0]:
				break		
	gear[gear_num].rotate(direction)
    
answer = 0
if gear[0][0] == 1:
	answer += 1
if gear[1][0] == 1:
	answer += 2
if gear[2][0] == 1:
	answer += 4
if gear[3][0] == 1:
	answer += 8
print(answer)