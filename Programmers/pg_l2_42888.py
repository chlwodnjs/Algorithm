def solution(record):
    answer = []
    check = []
    check_user = {}
    x = ['Enter', 'Leave']
    for i in range(len(record)):
        check.append(record[i].split())
        if check[i][0] != x[1]:
            check_user[check[i][1]] = check[i][2]

    for j in range(len(check)):
        if check[j][0] == x[0]:
            answer.append(check_user[check[j][1]] + "님이 들어왔습니다.")
        elif check[j][0] == x[1]:
            answer.append(check_user[check[j][1]] + "님이 나갔습니다.")

    return answer