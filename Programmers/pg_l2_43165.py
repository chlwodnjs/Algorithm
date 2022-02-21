answer = 0


def bt(numbers, target, idx, total):
    global answer
    if idx == len(numbers):
        if target == total:
            answer += 1
        return
    bt(numbers, target, idx + 1, total + numbers[idx])
    bt(numbers, target, idx + 1, total - numbers[idx])


def solution(numbers, target):
    global answer
    bt(numbers, target, 0, 0)
    return answer

# from collections import deque
# def solution(numbers, target):
#     answer = 0
#     q = deque([(0,0)])
#     while q:
#         x,y = q.popleft()
#         if y>len(numbers):
#             return answer
#         if y==len(numbers) and target == x:
#             answer +=1
#         q.append((x+numbers[y-1],y+1))
#         q.append((x-numbers[y-1],y+1))
