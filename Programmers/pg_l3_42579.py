def solution(genres, plays):
    answer = []
    dic = {}
    L = len(genres)
    for i in range(L):
        dic[genres[i]] = 0
    for i in range(L):
        dic[genres[i]] += plays[i]

    dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)

    for x, y in dic:
        check = []
        for i, (j, k) in enumerate(zip(genres, plays)):
            if x == j:
                check.append([k, i])

        check = sorted(check, key=lambda x: (-x[0], x[1]))
        answer.append(check[0][1])
        if len(check) != 1:
            answer.append(check[1][1])
    return answer
