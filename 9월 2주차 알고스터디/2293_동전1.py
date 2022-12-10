n,k = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))
coin.sort(reverse=True)
cnt = 0
ans = 0
def change(level):
    global cnt, ans
    if ans == k:
        cnt += 1
        return
    elif ans > k:
        return 
    if level == n-1:
        for i in range(k//coin[level]+1):
            ans += coin[level]*i
            if ans == k:
                cnt += 1
                ans -=coin[level]*i
            else:
                ans -= coin[level]*i
        return

    for i in range(k//coin[level]+1):
        ans += coin[level]*i
        change(level+1)
        ans -= coin[level]*i
change(0)
print(cnt)


