def solution(numbers):
    answer = numbers[:]
    for i in range(len(numbers)):
        exp = 0
        while numbers[i] > 0:
            if numbers[i] % 2 == 0:
                break
            else:
                numbers[i] //= 2
                exp += 1
        answer[i] += 2 ** exp
        if exp:
            answer[i] -= 2 ** (exp-1)

    return answer