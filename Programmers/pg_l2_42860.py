def solution(name):
    if set(name) == {'A'}:
        return 0
    a = ord('A')
    z = ord('Z')
    answer = float("inf")  # 양의무한대
    L = len(name) // 2
    for i in range(L):
        left_moved = name[-i:] + name[:-i]
        right_moved = name[i:] + name[:i]
        for n in [left_moved, right_moved[0] + right_moved[:0:-1]]:
            while n and n[-1] == 'A':
                n = n[:-1]

            row_move = i + len(n) - 1
            col_move = 0
            for c in map(ord, n):
                col_move += min(c - a, z - c + 1)

            answer = min(answer, row_move + col_move)

    return answer
