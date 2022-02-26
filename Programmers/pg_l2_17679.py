from collections import deque


def solution(m, n, board):
    answer = 0
    board = [list(board[i]) for i in range(m)]

    while 1:
        remove = [[0] * n for _ in range(m)]
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] and board[i][j] == board[i][j + 1] == board[i + 1][j] == board[i + 1][j + 1]:
                    remove[i][j], remove[i][j + 1], remove[i + 1][j], remove[i + 1][j + 1] = 1, 1, 1, 1

        count = 0
        for i in range(m):
            count += sum(remove[i])
        answer += count
        if count == 0:
            break
        for i in range(m - 1, -1, -1):
            for j in range(n):
                if remove[i][j]:
                    x = i - 1
                    while x >= 0 and remove[x][j]:
                        x -= 1
                    if x >= 0:
                        board[i][j] = board[x][j]
                        remove[x][j] = 1
                    if x < 0:
                        board[i][j] = 0
    return answer