from itertools import combinations


def solution(relation):
    rows = len(relation)
    columns = len(relation[0])
    res = []
    col = [_ for _ in range(columns)]

    for i in range(columns):
        for comb in combinations(col, i + 1):
            flag = 1
            for r in res:
                if not r - set(comb):
                    flag = 0
                    break
            if flag == 0:
                continue
            check = set([tuple([i[_] for _ in comb]) for i in relation])
            if len(check) == rows:
                res.append(set(comb))
    answer = len(res)
    return answer
