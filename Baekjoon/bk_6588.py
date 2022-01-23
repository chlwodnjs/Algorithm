m = 1000000
check = [0] * m

for i in range(2, int(m ** 0.5)+1):
    if check[i] == 0:
        for j in range(i * 2, m, i):
            if check[j] == 0:
                check[j] = 1

while 1:
    n = int(input())
    if n == 0:
        break
    for i in range(3, m):
        if check[i] == 0:
            if check[n - i] == 0:
                print("{0} = {1} + {2}".format(n, i, n - i))
                break
