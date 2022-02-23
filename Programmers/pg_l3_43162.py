from collections import deque

def solution(n, computers):
    answer = 0
    check = [0]*n
    for i in range(n):
        if check[i]==0:
            answer+=1
            q = deque([computers[i]])
            while q:
                x = q.popleft()
                for k in range(n):
                    if x[k] and not check[k]:
                        q.append((computers[k]))
                        check[k]=1
    return answer

# def solution(n, computers):
#     answer = 0
#     temp = []
#     for i in range(n):
#         temp.append(i)
#     for i in range(n):
#         for j in range(n):
#             if computers[i][j]:
#                 for k in range(n):
#                     if temp[k] == temp[i]:
#                         temp[k] = temp[j]
#     answer = len(set(temp))
#     return answer
