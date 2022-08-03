import sys

input=sys.stdin.readline

N,M=map(int,input().split())

not_hear=set([input().strip() for i in range(N)])
not_see=[input().strip() for i in range(M)]

cnt=0
for x in not_see:
    if x in not_hear:
        cnt+=1

print(cnt)