# 규칙 1. 원래 위치에 다 시 놓기
# 규칙 2. 3연속 안됨
n = int(input())
li = [0]

for _ in range(n):
    li.append(int(input()))
if n == 1:
    print(li[1])
else:
    dp = [0,li[1],li[1]+li[2]]
    for i in range(3, n+1):
        dp.append(max(dp[i - 1], dp[i - 3] + li[i - 1] + li[i], dp[i - 2] + li[i]))
    print(dp[n])
# 전전(n-2)까지의 최대 양 + 현재 양
# 전전전(n-3)까지의 최대 양 + 전(n-1)번째 양 + 현재 양
# 전(n-1)까지 최대 양 + 현재 와인을 마시지 않는 경우