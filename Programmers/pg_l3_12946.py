h_list = []


def hanoi(n, x, y):
    if n == 1:
        return h_list.append([x, y])
    else:
        hanoi(n - 1, x, 6 - x - y)
        h_list.append([x, y])
        hanoi(n - 1, 6 - x - y, y)


def solution(n):
    hanoi(n, 1, 3)
    return h_list


if __name__ == '__main__':
    n = int(input())
    print(solution(n))
