def solution(operations):
    answer = []
    check = []
    for i in operations:
        check.append(i.split())
    for i in range(len(check)):
        check[i][1] = int(check[i][1])

    for i in check:
        if i[0]=='I':
            answer.append(i[1])
        if i[0]=='D':
            if len(answer)>0:
                if i[1]==1:
                    answer.remove(max(answer))
                else:
                    answer.remove(min(answer))
    if not answer:
        answer =[0,0]
        return answer
    else:
        answer = [max(answer),min(answer)]
        return answer