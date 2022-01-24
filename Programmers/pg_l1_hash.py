def solution(participant, completion):
    check = 0
    dict = {}
    for i in participant:
        dict[hash(i)] = i
        check += hash(i)

    for j in completion:
        check -= hash(j)

    return dict[check]

#     participant.sort()
#     completion.sort()
#     for i in range(len(completion)):
#         if participant[i]!=completion[i]:
#             return participant[i]

#     return participant[-1]
