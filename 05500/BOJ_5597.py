nums = [num for num in range(1, 31)]

for _ in range(28):
    n = int(input())
    nums.remove(n)

print(min(nums))
print(max(nums))
