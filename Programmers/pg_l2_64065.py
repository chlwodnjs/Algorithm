def solution(s):
    answer = []
    s = s[2:-2]
    s = s.split("},{")
    s = sorted(s, key=len)
    for i in s:
        j = i.split(",")
        for k in j:
            if int(k) not in answer:
                answer.append(int(k))

    return answer