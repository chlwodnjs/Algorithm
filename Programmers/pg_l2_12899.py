def dfs(n, check, arr):
    if n < 3:
        check.append(arr[n])
        return
    check.append(arr[n % 3])
    dfs(n // 3 - 1, check, arr)


def solution(n):
    arr = '124'
    if n <= 3:
        return arr[n - 1]
    n -= 1
    check = []
    dfs(n, check, arr)

    return ''.join(reversed(check))
