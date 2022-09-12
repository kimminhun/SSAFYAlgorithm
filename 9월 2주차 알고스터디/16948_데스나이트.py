from collections import deque
dir_y = [-2,-2,0,0,2,2]
dir_x = [-1,1,-2,2,-1,1]
n = int(input())
arr = [[0]*n for _ in range(n)]
used = [[0]*n for _ in range(n)]
start_y,start_x,end_y,end_x = map(int,(input().split()))
q = deque()
used[start_y][start_x] = 1
q.append([start_y,start_x])
# arr[start_y][start_x] = 0
while q:
    if arr[end_y][end_x] != 0:
        break
    y,x = q.popleft()
    for i in range(6):
        dy = dir_y[i] + y
        dx = dir_x[i] + x
        if 0<= dy < n and 0<= dx < n and used[dy][dx]== 0:
            arr[dy][dx] = arr[y][x] +1
            used[dy][dx] = 1
            q.append([dy,dx])
if arr[end_y][end_x] == 0:
    print(-1)
else:
    print(arr[end_y][end_x])
