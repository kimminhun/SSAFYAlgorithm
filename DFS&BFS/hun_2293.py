import sys
input=sys.stdin.readline

if __name__=="__main__":
    n,k=map(int,input().split())
    ar=[int(input()) for _ in range(n)]
    dp=[0]*(k+1)
    dp[0]=1

    for num in ar:
        for i in range(1,k+1):
            if i-num>=0:
                dp[i]+=dp[i-num]
    print(dp[k])