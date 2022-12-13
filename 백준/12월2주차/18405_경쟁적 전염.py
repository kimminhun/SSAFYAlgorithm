from collections import deque

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

directx = [0, 0, 1, -1]
directy = [1, -1, 0, 0]

def bfs(s):
    q = deque()
    virus_lst = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] !=0:
                virus_lst.append((arr[i][j], i, j, 0))
                virus_lst = sorted(virus_lst)

    for i in range(len(virus_lst)):
        num, y, x, s = virus_lst[i]
        q.append((num, y, x, s))
    while q:
        num, y, x, s = q.popleft()
        for j in range(4):
            dy = directy[j]+y
            dx = directx[j]+x
            if not (0 <= dy < N and 0 <= dx < N): continue
            if arr[dy][dx] == 0:
                arr[dy][dx] = num
                q.append((num, dy, dx, s+1))

            if S == s:
                return


bfs(0)

print(arr[X-1][Y-1])
