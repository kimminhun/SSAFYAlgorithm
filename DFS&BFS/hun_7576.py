import sys
from collections import deque
input=sys.stdin.readline


def bfs():
    global answer
    que=deque()
    for i in range(m):
        for j in range(n):
            if ar[i][j]==1:
                que.append((i,j,0))

    while que:
        x,y,day=que.popleft()
        answer=day
        for i in range(4):
            cx=x+dx[i]
            cy=y+dy[i]
            if 0<=cx<m and 0<=cy<n :
                if ar[cx][cy]==0:
                    ar[cx][cy]=1
                    que.append((cx,cy,day+1))
    if checking():
        print(answer)
    else:
        print(-1)

def checking():
    for i in range(m):
        for j in range(n):
            if ar[i][j]==0:
                return False
    return True






dx=[0,0,1,-1]
dy=[1,-1,0,0]

n,m=map(int,input().split())

ar=[list(map(int,input().split())) for _ in range(m)]
answer=0
bfs()
