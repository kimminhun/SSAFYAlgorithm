from collections import deque
from operator import truediv
import sys


class Printer:
    def __init__(self,idx,point):
        self.idx=idx
        self.point=point

 

T=int(sys.stdin.readline())



for _ in range(T):
    N,M=map(int,sys.stdin.readline().split())
    
    ar=list(map(int,sys.stdin.readline().split()))
    printerlist=deque()
    
    for i,x in enumerate(ar):
           printerlist.append(Printer(i,x))

    answer=0

    while True:
        # print(printerlist[0].point)
        if printerlist[0].point==max(ar):
            answer+=1
            if printerlist[0].idx!=M:
                printerlist.popleft()
                tmp=ar.index(max(ar))
                del ar[tmp]
            else :
                print(answer)
                break
        else:
            printerlist.append(printerlist[0])
            printerlist.popleft()
    