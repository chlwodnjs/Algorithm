from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for n in course:
        if n > len(max(orders, key=len)):
            break
        arr = []
        for m in orders:
            m = sorted(m)
            if len(m) >= n:
                arr.extend(list(combinations(m, n)))
        check = sorted(Counter(arr).items(), key=lambda x: x[1], reverse=True)[0][1]
        for k, v in Counter(arr).items():
            if v == check and check >= 2:
                answer.append(''.join(k))
        answer.sort()
    return answer
