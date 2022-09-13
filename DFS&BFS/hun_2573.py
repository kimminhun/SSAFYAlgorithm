import sys
from collections import deque
input=sys.stdin.readline

dx=[0,0,1,-1]
dy=[1,-1,0,0]
que = deque()

def bfs(x,y):
    que.append((x,y))
    while que:
        x,y=que.popleft()
        visit[x][y]=True
        for i in range(4):
            cx=x+dx[i]
            cy=y+dy[i]
            if 0<=cx<n and 0<=cy<m:
                if ar[cx][cy]!=0 and not visit[cx][cy]:
                    visit[cx][cy]=True
                    que.append((cx,cy))
                elif ar[cx][cy]==0:
                    count[x][y]+=1




if __name__=='__main__':
    n,m=map(int,input().split())
    ar=[list(map(int,input().split())) for _ in range(n)]
    answer=0

    while True:
        visit=[[False]*m for _ in range(n)]
        count=[[0]*m for _ in range(n)]
        tmp=0
        for i in range(n):
            for j in range(m):
                if ar[i][j]!=0 and not visit[i][j]:
                    bfs(i,j)
                    tmp+=1

        for i in range(n):
            for j in range(m):
                ar[i][j]-=count[i][j]
                if ar[i][j]<0:
                    ar[i][j]=0
                count[i][j]=0

        if tmp>=2:
            break
        if tmp==0:
            day=0
            break

        answer+=1

    print(answer)


