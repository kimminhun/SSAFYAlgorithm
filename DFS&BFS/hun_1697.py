import sys
from collections import deque
input=sys.stdin.readline


def bfs():
    que=deque()
    que.append(now)
    while que:
        x=que.popleft()
        if x==finish:
            return cnt[x]
        if x-1>=0 and not visit[x-1]:
            visit[x-1]=True
            cnt[x-1]=cnt[x]+1
            que.append(x-1)
        if x+1<100001 and not visit[x+1]:
            visit[x+1]=True
            cnt[x+1]=cnt[x]+1
            que.append(x+1)
        if 2*x<100001 and not visit[2*x]:
            visit[2*x]=True
            cnt[2*x]=cnt[x]+1
            que.append(2*x)



if __name__=="__main__":
    now,finish=map(int,input().split())
    visit=[False]*(100001)
    cnt=[0]*(100001)
    print(bfs())
