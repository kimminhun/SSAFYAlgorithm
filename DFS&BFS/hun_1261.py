
from collections import deque




def bfs():
    que=deque()
    que.append((0,0))
    visit[0][0]=True
    while que:
        x,y=que.popleft()
        for i in range(4):
            cx=x+dx[i]
            cy=y+dy[i]
            if 0<=cx<m and 0<=cy<n and not visit[cx][cy]:
                visit[cx][cy] = True
                if ar[cx][cy]==0:
                    ar[cx][cy] = ar[x][y]
                    que.appendleft((cx,cy))
                else:
                    ar[cx][cy]=ar[x][y]+1
                    que.append((cx,cy))


if __name__=="__main__":
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    n,m=map(int,input().split())

    ar=[list(map(int,input().rstrip())) for _ in range(m)]
    visit=[[False]*n for _ in range(m)]

    bfs()

    print(ar[m-1][n-1])