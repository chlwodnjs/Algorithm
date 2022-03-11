def solution(n, s):
    if n > s:
        return [-1]

    check = divmod(s, n)
    answer = [check[0] for _ in range(n)]

    for i in range(check[1]):
        answer[i] += 1

    return sorted(answer)