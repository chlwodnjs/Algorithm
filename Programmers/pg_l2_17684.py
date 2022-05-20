import string


def solution(msg):
    dic = {st: i + 1 for i, st in enumerate(string.ascii_uppercase)}
    answer = []
    i = 0
    x = 2
    L = len(msg)
    check = 27
    while 1:
        while msg[i:i + x] in dic:
            x += 1
            if i + x - 1 > L:
                break
        answer.append(dic[msg[i:i + x - 1]])
        if i + x - 1 > L:
            break
        if msg[i:i + x] not in dic:
            dic[msg[i:i + x]] = check
            check += 1
            i += (x - 1)
            x = 2

    return answer