def solution(s):
    check = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for j in range(len(s)):
        for i in range(len(check)):
            if check[i] in s:
                s = s.replace(check[i], str(i))
    answer = int(s)
    return answer


if __name__ == '__main__':
    s = str(input())
    print(solution(s))
