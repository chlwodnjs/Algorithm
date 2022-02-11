from collections import deque


def solution(prices):
    answer = []
    q = deque(prices)

    while q:
        cnt=0
        x = q.popleft()
        for i in q:
            cnt += 1
            if x > i:
                break
        answer.append(cnt)
    return answer
