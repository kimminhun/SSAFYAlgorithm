from collections import deque
import sys
input=sys.stdin.readline

if __name__=="__main__":
    n=int(input())
    ar=[[] for _ in range(n+1)]
    visit=[0]*(n+1)

    for _ in range(n-1):
        a,b=map(int,input().split())
        ar[a].append(b)
        ar[b].append(a)

    # def dfs(start):
    #     for i in ar[start]:
    #         if visit[i]==0:
    #             visit[i]=start
    #             dfs(i)
    # dfs(1)
    # for i in range(2,len(visit)):
    #     print(visit[i])

    answer=[0]*(n+1)
    que=deque()
    que.append(1)
    def bfs():
        while que:
            x=que.popleft()
            for i in ar[x]:
                if answer[i]==0:
                    answer[i]=x
                    que.append(i)
    bfs()
    for i in range(2,len(answer)):
        print(answer[i])



