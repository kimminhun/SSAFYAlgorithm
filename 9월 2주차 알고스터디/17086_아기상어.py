# BFS
from collections import deque
n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
sample = []
maxi = 0
dir_x = [0,1,1,1,0,-1,-1,-1]
dir_y = [1,1,0,-1,-1,-1,0,1]
sharq = deque()
for y in range(n):
    for x in range(m):
        if arr[y][x] == 1:
            sharq.append([y,x])
while sharq:
    y,x = sharq.popleft()
    for i in range(8):
        dy = dir_y[i] + y
        dx = dir_x[i] + x
        if 0<= dy < n and 0<= dx < m and arr[dy][dx] == 0:
            arr[dy][dx] = arr[y][x] + 1
            sharq.append([dy,dx])
            maxi = arr[dy][dx]
print(maxi-1)

            


        
