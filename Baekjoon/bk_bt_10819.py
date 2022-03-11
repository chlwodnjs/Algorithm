from itertools import permutations

if __name__ == '__main__':
    N = int(input())
    check = list(map(int, input().split()))
    res = list(permutations(check, N))
    answer = []
    for i in res:
        flag = 0
        x = N - 1
        while x:
            flag += abs(i[x-1] - i[x])
            x -= 1
        answer.append(flag)
    print(max(answer))
