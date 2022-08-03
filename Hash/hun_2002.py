from re import X
import sys

input=sys.stdin.readline

n=int(input())

before=[input().strip() for i in range(n)]
after=[input().strip() for i in range(n)]
cnt=0
for i in range(n-1):
    for j in range(i,n):
        if before.index(after[i])>before.index(after[j]):
            cnt+=1
            break


print(cnt)