if __name__ == '__main__':
    K, N = map(int, input().split())
    check = [int(input()) for _ in range(K)]
    start = 1
    end = max(check)
    while start <= end:
        mid = (start + end) // 2
        flag = 0
        flag = sum(i // mid for i in check)
        if flag >= N:
            start = mid + 1
        else:
            end = mid - 1

    print(end)
