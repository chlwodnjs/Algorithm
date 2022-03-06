from itertools import combinations

def check_prime(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True

def solution(nums):
    answer = 0
    check = list(combinations(nums,3))
    for i in check:
        if check_prime(sum(i)):
            answer+=1
    return answer