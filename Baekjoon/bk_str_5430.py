from collections import deque


def sim():
    R = 0
    while check_q:
        ac = check_q.popleft()
        if ac == 'R':
            R += 1
        if ac == 'D':
            if q:
                if R % 2 == 0:
                    q.popleft()
                else:
                    q.pop()
            else:
                return 'error'
    if q:
        if R % 2 == 0:
            result = '[' + ",".join(q) + ']'
        else:
            q.reverse()
            result = '[' + ",".join(q) + ']'
        return result
    return 'error'


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        p = input()
        check_q = deque(p)
        dcnt = 0
        for i in check_q:
            if i == 'D':
                dcnt += 1

        N = int(input())
        check = input()[1:-1]
        if check:
            q = deque(check.split(','))
        else:
            q = deque(check)
        if len(q) == dcnt:
            print('[]')
            continue
        print(sim())
