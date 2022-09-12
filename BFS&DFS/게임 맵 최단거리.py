from collections import deque
maps = input(list())
def bfs():
    q = deque()
    q.append([0,0])
    while q:
        y,x = q.popleft()
        dir_y = [-1,1,0,0]
        dir_x = [0,0,1,-1]
        for i in range(4):
            dy = dir_y[i] + y
            dx = dir_x[i] + x
            if 0<= dy < len(maps) and 0<= dx < len(maps[0]) and maps[dy][dx] != 0 and [dy,dx]:
                maps[dy][dx] = maps[y][x]+1
                q.append([dy.dx])
bfs()
if maps[(len(maps)-1)][(len(maps[0])-1)] == 1:
    print(-1)
else:
    print(maps[(len(maps)-1)][(len(maps[0])-1)])

















# while q:
#     y,x = q.popleft()
#     cnt +=1
#     dir_y = [-1,1,0,0]
#     dir_x = [0,0,1,-1]
#     for i in range(4):
#         dy = dir_y[i] + y
#         dx = dir_x[i] + x
#         if 0<= dy < len(maps) and 0<= dx < len(maps[0]) and maps[dy][dx] != 0 and [dy,dx] not in used:

#             q.append([dy,dx]) 

