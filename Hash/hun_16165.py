import sys

N,M=map(int,sys.stdin.readline().split())
member_dict={}
for _ in range(N):
    groupname=sys.stdin.readline()
    k=int(sys.stdin.readline())
    newlist=[]
    for _ in range(k):
        newlist.append(sys.stdin.readline())
    newlist.sort()
    member_dict[groupname]=newlist

answer_list=[]
for _ in range(M):
    name=sys.stdin.readline()
    quiz=int(sys.stdin.readline())
    if(quiz==1):
        for x in member_dict:
            if name in member_dict[x]:
                answer_list.append(x.rstrip("\n"))
                break
    else:
        for x in member_dict[name]:
            answer_list.append(x.rstrip("\n"))

for x in answer_list:
    print(x)