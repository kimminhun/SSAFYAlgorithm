import sys
input=sys.stdin.readline



if __name__=="__main__":
    n=int(input())
    ar=[0]
    for _ in range(n):
        ar.append(int(input()))
    dp = [0]
    dp.append(ar[1])
    if n>1:
        dp.append(ar[1]+ar[2])
    for i in range(3,n+1):
        dp.append(max(dp[i-1],dp[i-3]+ar[i-1]+ar[i],dp[i-2]+ar[i]))
    print(dp[n])


