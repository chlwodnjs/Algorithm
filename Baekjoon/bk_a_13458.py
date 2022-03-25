N = int(input())
check = list(map(int, input().split()))
B, C = map(int, input().split())
result = 0

for i in range(N):
    if check[i] > 0:
        check[i] -= B
        result += 1
    if check[i] > 0:
        result += check[i] // C
        if check[i] % C:
            result += 1
print(result)
