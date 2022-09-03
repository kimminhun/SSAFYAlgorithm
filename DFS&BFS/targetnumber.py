from collections import deque

def solution(numbers, target):
    answer = dfs(numbers,0,0,target)
    return answer

def dfs(numbers,level,SUM,target):
    if level==len(numbers):
        if SUM==target:
            return 1
        else :
            return 0

    return dfs(numbers,level+1,SUM-numbers[level],target)+dfs(numbers, level + 1, SUM + numbers[level],target)

def solution2(numbers,target):
    answer=0
    que=deque()
    que.append([numbers[0],0])
    que.append([numbers[0]*-1,0])
    while que:
        tmp,idx=que.popleft()
        idx+=1
        if idx<len(numbers):
            que.append([tmp+numbers[idx],idx])
            que.append([tmp-numbers[idx],idx])
        else:
            if tmp==target:
                answer+=1
    return answer
