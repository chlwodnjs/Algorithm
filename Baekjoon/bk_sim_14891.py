from collections import deque


if __name__ == '__main__':
    circle = [deque(map(int, input())) for _ in range(4)]
    M = int(input())
    q = deque()
    for _ in range(M):
        q.append((list(map(int, input().split()))))

    while q:
        num, direct = q.popleft()
        num -= 1
        tmp_2 = circle[num][2]
        tmp_6 = circle[num][6]
        circle[num].rotate(direct)
        tmp_direct = direct

        direct = tmp_direct
        for i in range(num - 1, 0 - 1, -1):
            if circle[i][2] != tmp_6:
                tmp_6 = circle[i][6]
                direct *= -1
                circle[i].rotate(direct)
            else:
                break

        direct = tmp_direct
        for i in range(num + 1, 4):
            if circle[i][6] != tmp_2:
                tmp_2 = circle[i][2]
                direct *= -1
                circle[i].rotate(direct)
            else:
                break
    res = 0
    for i in range(4):
        if circle[i][0] == 1:
            res += (2 ** i)
    print(res)