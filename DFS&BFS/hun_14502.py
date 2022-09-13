import copy
import sys
from collections import deque
input=sys.stdin.readline

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def create(level):
    if level==3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if ar[i][j]==0:
                ar[i][j]=1
                create(level+1)
                ar[i][j]=0

def bfs():
    global answer
    que=deque()
    tmp=copy.deepcopy(ar)
    for i in range(n):
        for j in range(m):
            if tmp[i][j]==2:
                que.append((i,j))

    while que:
        x,y=que.popleft()
        for i in range(4):
            cx=x+dx[i]
            cy=y+dy[i]
            if 0<=cx<n and 0<=cy<m and tmp[cx][cy]==0:
                tmp[cx][cy]=2
                que.append((cx,cy))
    cnt=0
    for x in tmp:
        cnt+=x.count(0)

    answer=max(cnt,answer)




if __name__=="__main__":
    n,m=map(int,input().split())
    ar=[list(map(int,input().split())) for _ in range(n)]

    answer=0
    create(0)
    print(answer)