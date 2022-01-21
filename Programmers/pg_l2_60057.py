def solution(s):
    res = []
    if len(s) == 1:
        return 1

    for i in range(len(s) // 2):
        check_str = ''
        cnt = 1
        check = s[:i + 1]
        for j in range(i + 1, len(s), i + 1):
            if check == s[j:i + 1 + j]:
                cnt += 1
            else:
                if cnt == 1:
                    check_str += check
                else:
                    check_str += str(cnt) + check
                check = s[j:i + 1 + j]
                cnt = 1
        if cnt == 1:
            check_str += check
        else:
            check_str += str(cnt) + check

        res.append(len(check_str))

    answer = sorted(res)[0]
    return answer


if __name__ == '__main__':
    s = str(input())
    print(solution(s))
