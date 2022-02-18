from collections import deque


def solution(N, number):
    answer = 0
    q = deque()
    q.append([0])
    q.append([N])
    if number == N:
        return 1
    else:
        for cnt in range(2, 9):
            numbers = [int(str(N) * cnt)]

            for i in range(1, cnt):
                for j in q[i]:
                    for k in q[cnt - i]:
                        numbers.append(j + k)
                        numbers.append(j - k)
                        numbers.append(j * k)
                        if k:
                            numbers.append(j // k)
            check = numbers
            if number in check:
                answer = cnt
                break
            else:
                q.append(check)
        if answer:
            return answer
        else:
            return -1

