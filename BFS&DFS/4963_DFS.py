import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
def dfs(j,i):
    arr[j][i] = 2
    for z in range(8):
        di = dir_y[z] +i
        dj = dir_x[z] +j
        if 0<= di <y and 0<= dj <x and arr[dj][di] == 1:
            dfs(dj,di)


while (1):
    y,x = map(int, input().split())
    if y == 0 and x ==0:
        break
    arr = [list(map(int, input().split()))for _ in range(x)]
    dir_y = [-1,-1,0,1,1,1,0,-1]
    dir_x = [0,1,1,1,0,-1,-1,-1]
    cnt = 0
    for n in range(x):
        for m in range(y):
            if arr[n][m] == 1:
                dfs(n,m)
                cnt +=1
    print(cnt)