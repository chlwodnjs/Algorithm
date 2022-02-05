def solution(clothes):
    answer = 1
    dic = {}
    for i in clothes:
        dic[i[1]] = 0
    for i in clothes:
        dic[i[1]] += 1
    for i in dic.values():
        answer *= (i + 1)

    return answer - 1