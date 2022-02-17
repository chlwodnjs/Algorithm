import math


def solution(brown, yellow):
    answer = []
    check = yellow
    y_list = []
    for i in range(1, int(math.sqrt(check)) + 1):
        if check % i == 0:
            y_list.append([i, check // i])

    for i in zip(y_list):
        if (i[0][0] + i[0][1] + 2) * 2 == brown:
            answer = [i[0][1] + 2, i[0][0] + 2]
    return answer