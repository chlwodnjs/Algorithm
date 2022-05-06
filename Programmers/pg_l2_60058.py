def check_func(x):
    check = []

    for i in x:
        if i == '(':
            check.append(i)
        else:
            if not check:
                return False
            check.pop()
    return True


def solution(p):
    answer = ''
    if p == '':
        return ''
    check_1 = 0
    check_2 = 0
    for i in range(len(p)):
        if p[i] == '(':
            check_1 += 1
        else:
            check_2 += 1
        if check_1 == check_2:
            u = p[:i + 1]
            v = p[i + 1:]
            break
    if check_func(u):
        return u + solution(v)
    else:
        answer += '(' + solution(v) + ')'

        for j in u[1:-1]:
            if j == '(':
                answer += ')'
            else:
                answer += '('

    return answer

