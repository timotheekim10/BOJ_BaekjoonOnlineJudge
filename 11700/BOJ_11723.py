import sys

input = sys.stdin.readline

m = int(input())
s = set()

for _ in range(m):
  arr = list(input().split())
  cmd = arr[0]
  if cmd == 'add':
    s.add(int(arr[1]))
  elif cmd == 'remove':
    try:
      s.remove(int(arr[1]))
    except:
      pass
  elif cmd == 'check':
    if int(arr[1]) in s:
        print(1)
    else:
      print(0)
  elif cmd == 'toggle':
    if int(arr[1]) in s:
      s.remove(int(arr[1]))
    else:
      s.add(int(arr[1]))
  elif cmd == 'all':
    s = set([i for i in range(1,21)])
  else:
    s = set()