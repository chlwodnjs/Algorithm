def solution(n, lost, reserve):
    reserve = set(reserve)
    lost = set(lost)
    check_1 = reserve-lost
    check_2 = lost-reserve

    for i in check_1:
        if i-1 in check_2:
            check_2.remove(i-1)
        elif i+1 in check_2:
            check_2.remove(i+1)

    answer = n - len(check_2)
    return answer