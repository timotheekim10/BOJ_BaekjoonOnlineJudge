import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    note_1 = list(map(int, input().split()))
    m = int(input())
    note_2 = list(map(int, input().split()))
    
    note_1.sort()

    for num in note_2:
        start_idx, end_idx = 0, n-1
        ans = False
        while start_idx <= end_idx:
            mid = (start_idx + end_idx) // 2
            if num < note_1[mid]:
                end_idx = mid - 1
            elif num > note_1[mid]:
                start_idx = mid + 1
            else:
                ans = True
                break
        if ans:
            print(1)
        else:
            print(0)