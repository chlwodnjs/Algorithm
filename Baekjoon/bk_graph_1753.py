import sys
import heapq

INF = sys.maxsize


def dij():
    while q:
        d, node = heapq.heappop(q)
        for n, w in check[node]:
            flag = d + w
            if flag < dist[n]:
                dist[n] = flag
                heapq.heappush(q, (flag, n))


if __name__ == '__main__':
    V, E = map(int, input().split())
    V += 1
    K = int(input())
    check = [[] for _ in range(V)]
    dist = [INF] * V

    for _ in range(E):
        a, b, c = map(int, input().split())
        check[a].append((b, c))

    dist[K] = 0
    q = []
    heapq.heappush(q, (0, K))

    dij()

    for i in dist[1:]:
        if i != INF:
            print(i)
        else:
            print("INF")
