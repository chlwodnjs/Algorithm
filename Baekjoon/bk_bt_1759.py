def bt(x):
    if len(graph) == L:
        cnt1 = 0
        cnt2 = 0
        cnt1_list = ['a', 'e', 'i', 'o', 'u']
        for i in range(L):
            if graph[i] in cnt1_list:
                cnt1 += 1
            else:
                cnt2 += 1
        if cnt1 >= 1 and cnt2 >= 2:
            for i in range(L):
                print(graph[i], end='')
            print()
        return
    for i in range(x, C):
        if not visit[i]:
            graph.append(check[i])
            visit[i] = 1
            bt(i + 1)
            visit[i] = 0
            graph.pop()


if __name__ == '__main__':
    L, C = map(int, input().split())
    check = list(map(str, input().split()))
    check = sorted(check)
    graph = []
    visit = [0] * C
    bt(0)
