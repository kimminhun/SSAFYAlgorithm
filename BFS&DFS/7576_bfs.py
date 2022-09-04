# 백준 7576 토마토
from collections import deque
n,m = map(int, input().split())
arr = [list(map(int, input().split()))for _ in range(m)]
dir_y = [-1,0,1,0]
dir_x = [0,1,0,-1]
day_cnt = 0
q = deque([])
for y in range(m):
    for x in range(n):
        if arr[y][x] == 1:
            q.append([y,x])
def bfs():
    while q:
        y,x = q.popleft()
        for i in range(4):
            dy,dx = dir_y[i]+y, dir_x[i]+x
            if 0<= dy < m and 0<= dx < n and arr[dy][dx] ==0:
                arr[dy][dx] = arr[y][x] + 1
                q.append([dy,dx])
bfs()
maxi =0
bp =0
for y in range(m):
    if bp == 1:
        break
    for x in range(n):
        if arr[y][x] == 0:
            print(-1)
            bp = 1
            break
        if arr[y][x] > maxi:
            maxi = arr[y][x]
if bp == 0:
    print(maxi-1)