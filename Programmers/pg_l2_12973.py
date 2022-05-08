def solution(s):
    answer = -1
    check = []

    for i in s:
        if not check:
            check.append(i)

        else:
            if check[-1] == i:
                check.pop()
            else:
                check.append(i)

    if check:
        return answer + 1
    else:
        return answer + 2
