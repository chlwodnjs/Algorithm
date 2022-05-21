from collections import Counter


def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    s1 = [str1[i:i + 2] for i in range(len(str1) - 1) if str1[i:i + 2].isalpha()]
    s2 = [str2[i:i + 2] for i in range(len(str2) - 1) if str2[i:i + 2].isalpha()]
    if not s1 and not s2:
        return 65536

    c1 = Counter(s1)
    c2 = Counter(s2)
    sum1 = sum((c1 & c2).values())
    sum2 = sum((c1 | c2).values())
    answer = int((sum1 / sum2) * 65536)
    return answer