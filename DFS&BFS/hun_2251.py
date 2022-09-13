import sys
from collections import deque
input=sys.stdin.readline

def bfs(now):
    que=deque([now])
    visit[now]=True
    while que:
        x=que.popleft()
        if x==G:
            return cnt[G]
        if x+U<F+1 and not visit[x+U]:
            visit[x+U]=True
            cnt[x+U]=cnt[x]+1
            que.append(x+U)
        if x-D>0 and not visit[x-D]:
            visit[x-D]=True
            cnt[x-D]=cnt[x]+1
            que.append(x-D)
    if cnt[G]==0:
        return "use the stairs"






if __name__=="__main__":
    F,S,G,U,D=map(int,input().split())

    ar=[0]*(F+1)
    visit=[False]*(F+1)
    cnt=[0]*(F+1)
    answer=bfs(S)
    print(answer)


