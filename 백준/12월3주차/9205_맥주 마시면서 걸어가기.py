import sys
from collections import deque
def bfs(x0, y0, used):
    global flag
    flag = 0
    q = deque()
    q.append((x0, y0, used))

    while q:
        x, y, used = q.popleft()
        final_distance = abs(x - end[0]) + abs(y - end[1])
        if final_distance <= 1000:
            flag = 1
            break
        for i in range(len(store)):
            if used[i] == 1: continue
            distance = abs(store[i][0]-x) + abs(store[i][1] - y)
            if distance <= 1000:
                used[i] = 1
                q.append((store[i][0], store[i][1], used))

    return

T  = int(sys.stdin.readline())
for test_case in range(T):
    n = int(sys.stdin.readline())
    start = list(map(int, sys.stdin.readline().split()))
    store = []
    for _ in range(n):
        store.append(list(map(int, sys.stdin.readline().split())))

    end = list(map(int, sys.stdin.readline().split()))

    # used = [0] * len(store)


    bfs(start[0], start[1], [0]*len(store))
    if flag == 1:
        print('happy')
    else:
        print('sad')
