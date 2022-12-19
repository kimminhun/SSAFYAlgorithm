import sys
import heapq

N, E = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(N+1)]
for _ in range(E):
    # a 시작점, b 도착점, c 비용
    a,b,c = map(int, input().split())
    arr[a].append((b,c))
    arr[b].append((a,c))

x, y = map(int, input().split())

inf = int(21e8)

def dijkstra(start, end):
    heap = []
    result = [inf]*(N+1)

    heapq.heappush(heap, (0, start))
    result[start] = 0

    while heap:
        tmp_cost, tmp = heapq.heappop(heap)

        if result[tmp] < tmp_cost: continue

        for i in arr[tmp]:
            cost = tmp_cost + i[1]
            if cost < result[i[0]]:
                result[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))
    # print(result)
    return result[end]


total1 = 0
total2 = 0

total1 += dijkstra(1,x)
total1 += dijkstra(x,y)
total1 += dijkstra(y,N)

total2 += dijkstra(1,y)
total2 += dijkstra(y,x)
total2 += dijkstra(x,N)

# print(total2)
fin_total = min(total1, total2)
if fin_total >= inf:
    print(-1)
else:
    print(fin_total)