N = int(input())
TP = [list(map(int,input().split())) for _ in range(N)]
res = [0]*(N+1)
for i in reversed(range(N)):
    if TP[i][0] + i > N:
        res[i] = res[i+1]
    else:
        res[i] = max(res[i+1], res[i + TP[i][0]] + TP[i][1])
print(res[0])
