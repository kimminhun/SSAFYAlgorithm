# 빙산 / PyPy로 제출
from collections import deque
n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# land = [[0]*m for _ in range(n)]
dir_y = [-1,0,1,0]
dir_x = [0,1,0,-1]
land_cnt = 0
year_cnt = 0

def bfs(s,g):
    q = deque()
    q.append([s,g])
    while q:
        y,x = q.popleft()

        for i in range(4):
            dy = dir_y[i] + y
            dx = dir_x[i] + x
            if 0<= dy < n and 0<= dx < m and arr[dy][dx] > 0 and land[dy][dx] == 0:
                land[dy][dx] = 1
                q.append([dy,dx])

while(1):
    used = [[0]*m for _ in range(n)]
    land = [[0]*m for _ in range(n)]
    land_cnt = 0
    for y in range(n):
        for x in range(m):
            if arr[y][x] > 0 and land[y][x] == 0:
                land[y][x] = 1
                bfs(y,x)
                land_cnt += 1
    if land_cnt == 0:
        print(0)
        break
    elif land_cnt >= 2:
        print(year_cnt)
        break

    for y in range(n):
        for x in range(m):
            if arr[y][x] > 0:
                sea_cnt = 0
                for i in range(4):
                    dy = dir_y[i] + y
                    dx = dir_x[i] + x
                    if 0<= dy < n and 0<= dx < m and arr[dy][dx] <= 0:
                        sea_cnt += 1
                used[y][x] = arr[y][x] - sea_cnt
                if used[y][x] < 0:
                    used[y][x] = 0
    arr,used = used,arr
    year_cnt +=1





