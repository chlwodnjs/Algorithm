def solution(n):
    answer = ''
    while n:
        n , th = divmod(n,3)
        answer+=str(th)
    return int(answer,3)