def solution(board, moves):
    answer = 0
    check_list = []
    for i in range(len(moves)):
        for j in range(len(board)):
            if j + 1 == moves[i]:
                for x in range(len(board)):
                    if board[x][j] != 0:
                        check_list.append(board[x][j])
                        board[x][j] = 0

                        if len(check_list) >= 2:
                            if check_list[-1] == check_list[-2]:
                                check_list.pop()
                                check_list.pop()
                                answer += 2
                        break
    return answer