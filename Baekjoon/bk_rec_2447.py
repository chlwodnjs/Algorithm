def rec(n):
    graph = []
    L = len(n)
    for i in range(3 * L):
        if i // L == 1:
            graph.append(n[i % L] + " " * L + n[i % L])
        else:
            graph.append(n[i % L] * 3)
    return graph


if __name__ == '__main__':

    N = int(input())
    star = ["***", "* *", "***"]
    check = 0
    while N != 3:
        N = int(N / 3)
        check += 1

    for i in range(check):
        star = rec(star)
    print(*star, sep='\n')
