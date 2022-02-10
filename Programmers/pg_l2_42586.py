import math


def solution(progresses, speeds):
    answer = []
    prog = []
    L = len(progresses)

    for i in range(L):
        x = 100 - progresses[i]
        prog.append(math.ceil(x / speeds[i]))
    check = prog[0]
    cnt = 1
    for i in range(1, L):
        if check < prog[i]:
            answer.append(cnt)
            cnt = 1
            check = prog[i]
        else:
            cnt += 1
    answer.append(cnt)

    return answer
