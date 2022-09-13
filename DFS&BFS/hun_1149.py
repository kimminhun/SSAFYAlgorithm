if __name__=="__main__":
    n=int(input())
    ar=[list(map(int,input().split())) for _ in range(n)]

    dp=[[0]*3 for _ in range(n)]
    dp[0][0],dp[0][1],dp[0][2]=ar[0][0],ar[0][1],ar[0][2]

    for i in range(1,n):
        dp[i][0]=min(dp[i-1][1],dp[i-1][2])+ar[i][0]
        dp[i][1]=min(dp[i-1][2],dp[i-1][0])+ar[i][1]
        dp[i][2]=min(dp[i-1][1],dp[i-1][0])+ar[i][2]

    answer=min(dp[n-1])
    print(answer)
