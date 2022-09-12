#백준 알고스팟


n,m = map(int,input().split())
arr = [list(input()) for _ in range(m)]
dir_y = [-1,0,1,0]
dir_x = [0,1,0,-1]
used = [[0]*n for _ in range(m)]
used[0][0] = 1
mini = n*m
def dfs(y,x, cnt):   
    global  mini

    if cnt > mini:
        return
    if y ==m-1 and x == n-1:
        if cnt < mini:
            mini = cnt
        return
    for i in range(4):
        dy = dir_y[i] + y
        dx = dir_x[i] + x
        if 0<= dy <m and 0<= dx <n and used[dy][dx] != 1:
            used[dy][dx] = 1
            if arr[dy][dx] == '1':
                cnt +=1
            dfs(dy,dx,cnt)
            used[dy][dx] = 0
            if arr[dy][dx] == '1':
                cnt -=1
dfs(0,0,0)
print(mini)
        

