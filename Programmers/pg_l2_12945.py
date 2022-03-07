def solution(n):
    answer = 0
    check = [0]*(n+1)
    check[1]=1
    for i in range(2,n+1):
        check[i] = check[i-2]+check[i-1]
    answer = check[n]%1234567
    return answer