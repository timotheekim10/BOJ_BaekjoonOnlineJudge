import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

def binary_search(arr, x):
    start, end = 0, len(arr)
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
    return start

LIS = [float('-inf')]
for i in range(n):
    if LIS[-1] < a[i]:
        LIS.append(a[i])
    elif LIS[-1] > a[i]:
        idx = binary_search(LIS, a[i])
        LIS[idx] = a[i]

print(len(LIS) - 1)