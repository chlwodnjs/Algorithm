import sys

sys.setrecursionlimit(10 ** 6)


def dfs(num, result):
    visit[num] = 1
    check.append(num)
    next = graph[num]

    if visit[next] == 1:
        if next in check:
            result += check[check.index(next):]
        return
    else:
        dfs(next, result)


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        N = n + 1
        graph = [0] + list(map(int, input().split()))
        visit = [0] * N
        res = []

        for j in range(1, N):
            if visit[j] == 0:
                check = []
                dfs(j, res)

        answer = n - len(res)
        print(answer)
