from collections import deque


def solution(begin, target, words):
    if target not in words:
        return 0
    return bfs(words, begin, target)


def bfs(words, begin, target):
    q = deque()
    q.append((begin, 0))
    while q:
        word, cnt = q.popleft()
        if word == target:
            return cnt
        for wd in words:
            count = 0
            for i in range(len(word)):
                if word[i] == wd[i]:
                    count += 1
            if count == len(word) - 1:
                q.append((wd, cnt + 1))
    return 0
