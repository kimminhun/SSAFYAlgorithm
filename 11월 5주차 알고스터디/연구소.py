from collections import deque
import copy
import sys
# import time
# start = time.time()
input = sys.stdin.readline
n,m = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(n)]

dir_y = [-1,0,1,0]
dir_x = [0,1,0,-1]

def bfs():
    q = deque()
    arr = copy.deepcopy(li)
    global ans
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                q.append((i,j))
    while q:
        y,x = q.popleft()

        for i in range(4):
            dy = y + dir_y[i]
            dx = x + dir_x[i]

            if dy <0 or dy >= n or dx <0 or dx >= m:
                continue
            if arr[dy][dx] == 0:
                arr[dy][dx] = 2
                q.append((dy,dx))
    space_cnt = 0
    for i in range(n):
        space_cnt += arr[i].count(0)
    ans = max(ans, space_cnt)

ans = 0
def dfs(wallCnt):
    if wallCnt == 3:
        bfs()
        return 
    for i in range(n):
        for j in range(m):
            if li[i][j] == 0:
                li[i][j] = 1
                dfs(wallCnt+1)
                li[i][j] = 0

dfs(0)
print(ans)
# end = time.time()
# print(f"{end - start:.5f} sec")