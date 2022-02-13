import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while len(scoville) > 1:
        answer += 1
        x = heapq.heappop(scoville)
        y = heapq.heappop(scoville)
        heapq.heappush(scoville, x + y * 2)
        if scoville[0] >= K:
            return answer

    return -1