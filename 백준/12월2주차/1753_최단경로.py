import heapq

# 메모리 문제 해결을 위해 heapq로 수정

def select_ky():
    Min = int(21e8)
    minidx = 0
    for i in range(V):
        if used[i] == 0 and result[i] < Min:
            Min = result[i]
            minidx = i
    return minidx


def dijkstra(K):
    # 시작점을 경유지로 놓기
    heapq.heappush(heap, (0, K-1))
    result[K-1] = 0

    # heapq에서 최소비용을 다음 경유지로 선택
    while heap:
        # 경유지까지 비용과 경유지
        tmp_cost, ky = heapq.heappop(heap)

        if result[ky] < tmp_cost: continue

        for i in arr[ky]:
            # print(i)
            cost=tmp_cost+i[1]
            if cost<result[i[0]]:
                result[i[0]] = cost
                heapq.heappush(heap,(cost,i[0]))



V, E = map(int, input().split())
K = int(input())
arr = [[] for _ in range(V)]
used = [0] * V
result = [21e8] * V
heap=[]


for _ in range(E):
    u, v, w = map(int, input().split())
    arr[u-1].append((v-1,w))

dijkstra(K)


for i in range(V):
    if result[i] == 21e8:
        result[i] = 'INF'
print(*result, sep='\n')