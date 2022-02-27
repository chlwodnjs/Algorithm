def solution(tickets):
    answer = []
    tickets = sorted(tickets)
    answer.append('ICN')
    dfs('ICN', tickets, answer)

    return answer


def dfs(start, tickets, answer):
    L = len(tickets)
    if not tickets:
        return answer
    for i in range(L):
        if start == tickets[i][0]:
            end = tickets[i][1]
            tickets.pop(i)
            answer.append(end)
            temp = dfs(end, tickets, answer)
            if temp:
                return temp
            answer.pop(-1)
            tickets.insert(i, [start, end])

