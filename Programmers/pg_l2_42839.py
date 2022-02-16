from itertools import permutations


def checkPrime(x):
    for i in range(2, x - 1):
        if x % i == 0:
            break
    else:
        return x


def solution(numbers):
    answer = 0
    res = []
    check = sorted(numbers, reverse=True)
    for i in range(1, len(check) + 1):
        res += list(permutations(check, i))

    wh = []
    fin = []
    for i in res:
        kk = ''
        for j in range(len(i)):
            kk += i[j]
        wh.append(kk)

    for i in range(len(wh)):
        wh[i] = int(wh[i])
        if wh[i] not in fin:
            fin.append(wh[i])

    for i in fin:
        if 1 < i == checkPrime(i):
            answer += 1

    return answer