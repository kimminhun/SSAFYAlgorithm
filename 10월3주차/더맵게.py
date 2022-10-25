

import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0]<K and len(scoville)!=1:
        a=heapq.heappop(scoville)
        b=heapq.heappop(scoville)*2
        tmp=a+b
        heapq.heappush(scoville,tmp)
        answer+=1
    if  scoville[0]<K:
        answer=-1
    return answer


