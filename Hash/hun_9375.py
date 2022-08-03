import sys

input=sys.stdin.readline

t=int(input())


while t>0:
    cloth_dict={}
    n=int(input())
    for _ in range(n):
        a,b=input().split()
        if b in cloth_dict:
            cloth_dict[b]+=1
        else :
            cloth_dict[b]=1

    result=1
    for x in cloth_dict:
        result*=(cloth_dict[x]+1)
    print(result-1)
    t-=1


