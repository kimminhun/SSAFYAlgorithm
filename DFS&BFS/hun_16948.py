import sys
from collections import deque
input=sys.stdin.readline

def bfs():
    que=deque()
    que.append((sx,sy))
    ar[sx][sy]=1
    while que:
        x,y=que.popleft()
        if x==fx and y==fy:
            break
        for i in range(len(dx)):
            cx=x+dx[i]
            cy=y+dy[i]
            if 0<=cx<n and 0<=cy<n and ar[cx][cy]==0:
                ar[cx][cy]=ar[x][y]+1
                que.append((cx,cy))

if __name__=="__main__":
    n=int(input())
    ar=[[0]*n for _ in range(n)]

    sx,sy,fx,fy=map(int,input().split())

    dx=[-2,-2,0,0,2,2]
    dy=[-1,1,-2,2,-1,1]

    bfs()
    print(ar[fx][fy]-1)