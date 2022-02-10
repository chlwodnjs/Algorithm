from collections import deque


def solution(priorities, location):
    answer = 0
    q = deque()
    for i in range(len(priorities)):
        q.append((priorities[i], i))
    while q:
        x, y = q.popleft()

        if q and x < max(q)[0]:
            q.append((x, y))
        else:
            answer += 1
            if y == location:
                return answer
