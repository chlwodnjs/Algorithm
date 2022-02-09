def bt(x, res):
    global cnt
    if x == N:
        if res == S:
            cnt += 1
        return
    bt(x + 1, res)
    bt(x + 1, res + nlist[x])


if __name__ == '__main__':
    N, S = map(int, input().split())
    nlist = list(map(int, input().split()))
    cnt = 0
    bt(0, 0)
    if S == 0: cnt -= 1
    print(cnt)

# from itertools import combinations
#
# n, s = map(int, input().split())
# arr = list(map(int, input().split()))
# cnt = 0
# for i in range(1, n+1):
#     comb = combinations(arr, i)
#
#     for x in comb:
#         if sum(x) == s:
#             cnt += 1
#
# print(cnt)