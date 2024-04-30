import sys
from collections import deque

input = sys.stdin.readline

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def rotate_and_melting(board, len_board, l):
    new_board = [[0] * len_board for _ in range(len_board)]
    r_size = 2 ** l
    for y in range(0, len_board, r_size):
        for x in range(0, len_board, r_size):
            for i in range(r_size):
                for j in range(r_size):
                    new_board[y + j][x + r_size - i - 1] = board[y + i][x + j]

    board = new_board
    melting_list = []
    for y in range(len_board):
        for x in range(len_board):
            ice_count = 0
            for d in range(4):
                ny = y + dy[d]
                nx = x + dx[d]

                if 0<=ny<len_board and 0<=nx<len_board and board[ny][nx] > 0:
                    ice_count += 1

            if ice_count < 3 and board[y][x] != 0:
                melting_list.append((y, x))

    for y, x in melting_list:
        board[y][x] -= 1

    return board

def bfs(board, len_board):
    visited = [[False] * len_board for _ in range(len_board)]
    ice_sum = 0
    max_area_count = 0
    for y in range(len_board):
        for x in range(len_board):
            area_count = 0
            if visited[y][x] or board[y][x] == 0:
                continue
            q = deque()
            q.append((y, x))
            visited[y][x] = True

            while q:
                sy, sx = q.popleft()
                ice_sum += board[sy][sx]
                area_count += 1

                for d in range(4):
                    ny = sy + dy[d]
                    nx = sx + dx[d]
                    if 0<=ny<len_board and 0<=nx<len_board and not visited[ny][nx] and board[ny][nx] != 0:
                        visited[ny][nx] = True
                        q.append((ny, nx))

            max_area_count = max(max_area_count, area_count)

    print(ice_sum)
    print(max_area_count)


n, q = map(int, input().split())
len_board = 2 ** n
board = [list(map(int, input().split())) for _ in range(len_board)]
l_list = list(map(int, input().split()))

for l in l_list:
    board = rotate_and_melting(board, len_board, l)

bfs(board, len_board)