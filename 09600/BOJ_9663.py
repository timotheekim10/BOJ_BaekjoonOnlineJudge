import sys

input = sys.stdin.readline

n = int(input())
x = [0]*(n+1)
ans = 0

def backtracking(k, col):
	for i in range(1, k):
		if x[i]==col or abs(i-k)==abs(x[i]-col):
			return False
	return True
	
def nQueen(k):
	global ans
	if k > n:
		ans += 1
		return
	for col in range(1, n+1):
		if backtracking(k, col):
			x[k] = col
			nQueen(k+1)

nQueen(1)
print(ans)