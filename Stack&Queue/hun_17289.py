#오큰수
from collections import deque

n=int(input())
ls=list(map(int,input().split()))

ar=[-1]*n

stack=deque()

for i in range(n):
    while stack and stack[-1][0]<ls[i]:
        tmp,idx=stack.pop()
        ar[idx]=ls[i]
    stack.append([ls[i],i])

print(ar)
