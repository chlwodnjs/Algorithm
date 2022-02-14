def solution(jobs):
    answer = 0
    check = 0
    jobs.sort(key=lambda x: x[1])
    L = len(jobs)

    while len(jobs):
        for i in range(len(jobs)):
            if jobs[i][0] <= check:
                check += jobs[i][1]
                answer += check
                answer -= jobs[i][0]
                jobs.remove(jobs[i])
                break
            if i == len(jobs) - 1:  # 해당 시간에 작업이 아직 x
                check += 1

    answer //= L
    return answer