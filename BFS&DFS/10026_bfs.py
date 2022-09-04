from collections import deque
n = int(input())
arr = [list(input())for _ in range(n)]
used = [[0]*n for _ in range(n)]
dir_y = [-1,0,1,0]
dir_x = [0,1,0,-1]
def bfs(y,x,z):
    q = deque([])
    used[y][x] += 1
    q.append([y,x])
    while q:
        y,x = q.popleft()
        for i in range(4):
            dy = dir_y[i] + y
            dx = dir_x[i] + x
            if 0<= dy < n and 0<= dx < n and used[dy][dx] ==z and arr[dy][dx] == arr[y][x]:
                used[dy][dx] +=1
                q.append([dy,dx])
cnt,gbcnt  = 0,0
for y in range(n):
    for x in range(n):
        if used[y][x] != 1:
            bfs(y,x,0)
            cnt += 1
for y in range(n):
    for x in range(n):
        if arr[y][x] =='R':
            arr[y][x] = 'G'
for y in range(n):
    for x in range(n):
        if used[y][x] != 2:
            bfs(y,x,1)
            gbcnt += 1            

print(cnt, gbcnt)
         