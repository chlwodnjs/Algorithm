from copy import deepcopy


def move(board, dir):
    if dir == 0:
        for i in range(n):
            check = n - 1
            for j in reversed(range(n - 1)):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if not board[i][check]:
                        board[i][check] = tmp
                    elif board[i][check] == tmp:
                        board[i][check] = tmp * 2
                        check -= 1
                    else:
                        check -= 1
                        board[i][check] = tmp

    elif dir == 1:
        for i in range(n):
            check = 0
            for j in range(1, n):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if not board[i][check]:
                        board[i][check] = tmp
                    elif board[i][check] == tmp:
                        board[i][check] = tmp * 2
                        check += 1
                    else:
                        check += 1
                        board[i][check] = tmp

    elif dir == 2:
        for j in range(n):
            check = n - 1
            for i in reversed(range(n - 1)):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if not board[check][j]:
                        board[check][j] = tmp
                    elif board[check][j] == tmp:
                        board[check][j] = tmp * 2
                        check -= 1
                    else:
                        check -= 1
                        board[check][j] = tmp

    else:
        for j in range(n):
            check = 0
            for i in range(1, n):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[check][j] == 0:
                        board[check][j] = tmp
                    elif board[check][j] == tmp:
                        board[check][j] = tmp * 2
                        check += 1
                    else:
                        check += 1
                        board[check][j] = tmp

    return board


def dfs(board, cnt):
    global ans
    if cnt == 5:
        for i in range(n):
            for j in range(n):
                res.append(board[i][j])

        return

    for i in range(4):
        tmp_board = move(deepcopy(board), i)
        dfs(tmp_board, cnt + 1)


if __name__ == '__main__':
    n = int(input())

    graph = [list(map(int, input().split())) for _ in range(n)]

    res = []
    dfs(graph, 0)
    print(max(res))
