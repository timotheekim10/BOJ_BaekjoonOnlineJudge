import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

a.sort()

ans = 0

for i in range(n):
    arr = a[:i] + a[i+1:]
    left, right = 0, len(arr)-1

    while left < right:
        add_val = arr[left] + arr[right]
        if add_val == a[i]:
            ans += 1
            break
        elif add_val > a[i]:
            right -= 1
        else:
            left += 1

print(ans)