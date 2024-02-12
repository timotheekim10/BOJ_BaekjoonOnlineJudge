import sys
input = sys.stdin.readline

n = int(input())

n_set = set(map(int, input().split()))

m = int(input())

m_list = list(map(int, input().split()))

for i in m_list:
    print(int(i in n_set))