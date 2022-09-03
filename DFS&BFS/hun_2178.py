from collections import deque

n,m=map(int,input().split())
ar=[list(map(int,input())) for _ in range(n)]
dist=[[0]*m for _ in range(n)]

def bfs(x,y):
    que=deque()
    que.append((x,y))
    dx=[0,0,-1,1]
    dy=[1,-1,0,0]
    while que:
        x,y=que.popleft()
        for i in range(4):
            cx=x+dx[i]
            cy=y+dy[i]
            if 0<=cx<n and 0<=cy<m and ar[cx][cy]==1 and dist[cx][cy] == 0:
                que.append((cx,cy))
                dist[cx][cy]=dist[x][y]+1
dist[0][0] = 1
bfs(0,0)

print(dist[n-1][m-1])
