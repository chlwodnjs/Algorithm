def solution(citations):
    answer = 0
    m = 0
    for h in range(max(citations)):
        check_1 = 0
        check_2 = 0
        for i in citations:
            if i >= h:
                check_1 += 1
            else:
                check_2 += 1
        if check_1 >= h and check_2 < h:
            if h > m:
                m = h
    answer = m
    return answer

