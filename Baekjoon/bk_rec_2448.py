import math


def rec(x):
    for i in range(len(check)):
        check.append(check[i] * 2)
        check[i] = (" " * x + check[i] + " " * x)


if __name__ == '__main__':
    check = ['  *   ', ' * *  ', '***** ']
    N = int(input())
    K = int(math.log(int(N / 3), 2))
    for i in range(K):
        rec(pow(2, i)*3)
    for i in range(N):
        print(check[i])
