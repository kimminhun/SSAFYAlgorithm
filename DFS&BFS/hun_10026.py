import sys
sys.setrecursionlimit(10000)

input=sys.stdin.readline

n=int(input())

ar=[list(input()) for _ in range(n)]
visit=[[False]*n for _ in range(n)]

dx=[0,0,-1,1]
dy=[1,-1,0,0]

def dfs(x,y):
    visit[x][y]=True
    for i in range(4):
        cx=x+dx[i]
        cy=y+dy[i]
        if 0<=cx<n and 0<=cy<n and not visit[cx][cy] and ar[x][y]==ar[cx][cy]:
            dfs(cx,cy)
    return 1


def dfs2(x,y):
    visit[x][y]=True
    c=ar[x][y]
    for i in range(4):
        cx=x+dx[i]
        cy=y+dy[i]
        if 0<=cx<n and 0<=cy<n :
            if c=='R' or c=='G':
                if (ar[cx][cy]=='R' or ar[cx][cy]=='G') and not visit[cx][cy]:
                    dfs2(cx,cy)
            else:
                if ar[cx][cy]==c and not visit[cx][cy]:
                    dfs2(cx,cy)
    return 1


cnt=0
cnt2=0

for i in range(n):
    for j in range(n):
        if not visit[i][j]:
            cnt+=dfs(i,j)

visit=[[False]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visit[i][j]:
            cnt2+=dfs2(i,j)

print(cnt,cnt2)