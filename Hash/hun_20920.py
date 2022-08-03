import sys

input=sys.stdin.readline

N,M=map(int,input().split())

word_dict={}

for _ in range(N):
    words=input().strip()

    if len(words)<M:
        continue
    if word_dict.get(words):
        word_dict[words][0]+=1
    else:
        word_dict[words]=[1,len(words),words]
    
answer=sorted(word_dict.items(),key=lambda x:(-x[1][0],-x[1][1],x[1][2]))

for x in answer:
    print(x[0])

