def check():
    for i in range(1, n + 1):
        temp = i
        for j in range(1, h + 1):
            if s[j][temp] == 1:
                temp += 1
            elif s[j][temp - 1] == 1:
                temp -= 1
        if temp != i:
            return 0
    return 1


def dfs(num, cnt):
    global result
    if result < 5:
        return
    if num == cnt:
        if check():
            result = cnt
        return
    for bb in range(1, n):
        for aa in range(1, h + 1):
            if s[aa][bb - 1] == 0 and s[aa][bb + 1] == 0 and s[aa][bb] == 0:
                s[aa][bb] = 1
                dfs(num, cnt + 1)
                s[aa][bb] = 0
                while aa < h:
                    if s[aa][bb - 1] or s[aa][bb + 1]:
                        break
                    aa += 1


if __name__ == '__main__':
    n, m, h = map(int, input().split())
    s = [[0] * (n + 1) for _ in range(h + 1)]
    result = 5
    for i in range(m):
        a, b = map(int, input().split())
        s[a][b] = 1
    for i in range(4):
        dfs(i, 0)

    print(result if result < 5 else -1)
