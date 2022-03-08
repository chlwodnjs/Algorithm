def solution(id_list, report, k):
    answer = []

    check1 = {}
    check2 = {}
    for i in id_list:
        check1[i] = set()
        check2[i] = set()
    for x in report:
        check = x.split(' ')
        check1[check[1]].add(check[0])
        check2[check[0]].add(check[1])

    for i in id_list:
        cnt = 0
        for j in check2[i]:
            if len(check1[j]) >= k:
                cnt += 1
        answer.append(cnt)
    return answer