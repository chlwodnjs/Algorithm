def solution(numbers):
    answer = ''
    check = list(map(str, numbers))
    check = (sorted(check, key=lambda x: x * 3, reverse=True))
    for i in check:
        answer += str(i)

    return str(int(answer))