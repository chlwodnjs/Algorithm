from itertools import permutations
import re


def solution(user_id, banned_id):
    answer = ''
    res = set(answer)
    check_length = len(banned_id)
    combination = list(permutations(user_id, check_length))
    for comb in combination:
        check = 0
        for i in range(check_length):
            if not re.match(banned_id[i].replace('*', '.'), comb[i]):
                break
            elif len(banned_id[i]) != len(comb[i]):
                break
            else:
                check += 1
        if check == check_length:
            res.add(frozenset(comb))

    return len(res)
