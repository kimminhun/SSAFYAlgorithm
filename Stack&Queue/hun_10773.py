from collections import deque
import sys

k=int(input())


stk=deque()

for _ in range(k):
    tmp=int(sys.stdin.readline())
    if(tmp!=0):
        stk.append(tmp)
    else:
        stk.pop()
    
print(sum(stk))