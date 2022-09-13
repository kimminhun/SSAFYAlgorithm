import sys
input=sys.stdin.readline


#시간초과
def dfs(level,idx):
    global answer
    if level==n//2:
        ascore, bscore = 0, 0
        for i in range(n):
            for j in range(i+1,n):
                if visit[i] and visit[j] :
                    ascore += (ar[i][j]+ar[j][i])
                elif not visit[i] and not visit[j]:
                    bscore += (ar[i][j]+ar[j][i])
        answer = min(answer, abs(ascore - bscore))
        return
    for i in range(idx,n):
        if not visit[i]:
            visit[i]=True
            dfs(level+1,idx + 1)
            visit[i]=False


if __name__=="__main__":
    n=int(input())
    ar=[list(map(int,input().split())) for _ in range(n)]
    visit=[False]*n
    answer=int(1e9)
    dfs(0,0)

    print(answer)


