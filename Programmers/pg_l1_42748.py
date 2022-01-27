def solution(array, commands):
    answer = []

    for i in commands:
        I = i[0]
        J = i[1]
        K = i[2]
        check = array[I - 1:J]
        answer.append(sorted(check)[K - 1])

    return answer