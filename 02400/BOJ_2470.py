import sys

input = sys.stdin.readline

n = int(input())
sol = list(map(int, input().split()))

sol.sort()

left, right = 0, n-1
min = float('inf')
result = []

while left < right:
    ans = sol[left] + sol[right]
    
    if abs(ans) < min:
        min = abs(ans)
        result = [sol[left], sol[right]]
    
    if ans < 0:
        left += 1
    elif ans > 0:
        right -= 1
    else:
        break

print(*result)