board = input()

x_num = 0
answer = ''

for i in range(len(board)):
    if board[i] == '.':
        aaaa_num = x_num//4
        if x_num%4 == 0:
            answer += 'AAAA' * aaaa_num
            answer += '.'
            x_num = 0
        elif x_num%4 == 3:
            print(-1)
            exit(0)
        elif x_num%4 == 2:
            answer += 'AAAA' * aaaa_num + 'BB'
            answer += '.'
            x_num = 0
        else:
            print(-1)
            exit(0)
    else:
        x_num += 1
        if i == len(board)-1:
            aaaa_num = x_num//4
            if x_num%4 == 0:
                answer += 'AAAA' * aaaa_num
            elif x_num%4 == 3:
                print(-1)
                exit(0)
            elif x_num%4 == 2:
                answer += 'AAAA' * aaaa_num + 'BB'
            else:
                print(-1)
                exit(0)

print(answer)