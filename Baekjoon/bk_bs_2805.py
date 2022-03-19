if __name__ == '__main__':
    N, M = map(int, input().split())
    graph = list(map(int, input().split()))
    start = 0
    end = max(graph)
    res = []
    while start <= end:
        mid = (start + end) // 2
        flag = 0

        flag = sum(i - mid if i > mid else 0 for i in graph)
        if flag == M:
            res.append(mid)
            break
        elif flag > M:
            res.append(mid)
            start = mid + 1
        else:
            end = mid - 1

    print(max(res))
