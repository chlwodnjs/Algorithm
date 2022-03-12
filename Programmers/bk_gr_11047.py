if __name__ == '__main__':
    N, K = map(int, input().split())
    arr = [int(input()) for _ in range(N)]
    res = 0
    for i in reversed(range(N)):
        res += K // arr[i] 
        K = K % arr[i]

    print(res)
