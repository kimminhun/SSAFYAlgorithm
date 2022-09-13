def dfs(x,y):
    global cnt
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    visit[x][y]=True
    for i in range(4):
        cx=x+dx[i]
        cy=y+dy[i]
        if 0<=cx<n and 0<=cy<n and not visit[cx][cy] and ar[cx][cy]==1:
            cnt += 1
            dfs(cx,cy)



n=int(input())

ar=[list(map(int,input())) for _ in range(n)]
visit=[[False]*n for _ in range(n)]

answer=[]

for i in range(n):
    for j in range(n):
        if not visit[i][j]and ar[i][j]==1:
            cnt=1
            dfs(i,j)
            answer.append(cnt)

answer.sort()
print(len(answer))
print(*answer,sep='\n')