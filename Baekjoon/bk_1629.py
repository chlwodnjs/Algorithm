def pow(x, y):
    if y == 1:
        return x % z
    tmp = pow(x, y // 2)
    if y % 2 == 0:
        return tmp * tmp % z
    else:
        return tmp * tmp * x % z


if __name__ == '__main__':
    x, y, z = map(int, input().split())
    res = pow(x, y)
    print(res)
