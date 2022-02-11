from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    check = [0] * bridge_length
    q = deque(truck_weights)
    flag = 0
    while check:
        flag -= check.pop(0)
        if q:
            if flag + q[0] <= weight:
                flag += q[0]
                check.append(q.popleft())
            else:
                check.append(0)
        answer += 1
    return answer
