from collections import deque
import copy
directx = [1, -1, 0, 0]
directy = [0, 0, 1, -1]

def dfs(level):
    global max_cnt
    if level == 3:
        bfs()
        if max_cnt < cnt:
            max_cnt = cnt
        return
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                dfs(level+1)
                arr[i][j] = 0


def bfs():
    global cnt
    q = deque()
    tmp = copy.deepcopy(arr)
    for i in range(N):
        for j in range(M):
            if tmp[i][j] == 2:
                q.append((i, j))
    while q:
        y, x = q.popleft()
        for i in range(4):
            dy = y+directy[i]
            dx = x+directx[i]

            if not (0<= dy < N and 0<= dx < M): continue
            if tmp[dy][dx] == 0:
                tmp[dy][dx] = 2
                q.append((dy,dx))
    cnt = 0
    for i in range(N):
        for j in range(M):
            if tmp[i][j] == 0:
                cnt += 1
    # result = max(result, cnt)

max_cnt = 0
# result = 0
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dfs(0)
print(max_cnt)
