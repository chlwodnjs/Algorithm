def solution(answers):
    answer = []
    caseA = [1, 2, 3, 4, 5]
    caseB = [2, 1, 2, 3, 2, 4, 2, 5]
    caseC = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    while len(caseA) < 10001:
        for i in range(5):
            caseA.append(caseA[i])
        for j in range(8):
            caseB.append(caseB[j])
        for c in range(10):
            caseC.append(caseC[c])

    caseA_cnt = 0
    caseB_cnt = 0
    caseC_cnt = 0

    for k in range(len(answers)):
        if answers[k] == caseA[k]:
            caseA_cnt += 1
        if answers[k] == caseB[k]:
            caseB_cnt += 1
        if answers[k] == caseC[k]:
            caseC_cnt += 1
    check = []
    check.append(caseA_cnt)
    check.append(caseB_cnt)
    check.append(caseC_cnt)

    for i in range(3):
        if check[i] == max(check):
            answer.append(i + 1)

    return answer