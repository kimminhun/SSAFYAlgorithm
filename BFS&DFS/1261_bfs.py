#백준 알고스팟

from collections import deque

n,m = map(int,input().split())
arr = [list(map (int, input())) for _ in range(m)]
dir_y = [-1,0,1,0]
dir_x = [0,1,0,-1]
dist = [[-1]*n for _ in range(m)]

def bfs(y,x):
    queue = deque()
    queue.append((y,x))
    dist[0][0] = 0
    while queue:
        y,x = queue.popleft()
        for i in range(4):
            dy = dir_y[i] + y
            dx = dir_x[i] + x
            if 0<= dy <m and 0<= dx <n:
                if dist[dy][dx] == -1:
                    if arr[dy][dx] ==0:
                        dist[dy][dx] = dist[y][x]
                        queue.appendleft((dy,dx))
                    else:
                        dist[dy][dx] = dist[y][x] +1
                        queue.append((dy,dx))
bfs(0,0)
print(dist[m-1][n-1])
