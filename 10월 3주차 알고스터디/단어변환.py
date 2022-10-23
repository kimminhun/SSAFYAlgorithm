from collections import deque
def similar(now, t):
    cnt = 0
    for i in range(len(now)):
        if now[i] != t[i]:
            cnt += 1
        if cnt >1:
            return False
    if cnt == 0:
        return False
    if cnt == 1:
        return True
answer = 0           
def solution(begin, target, words):
    global answer
    if target not in words:
        return answer
    q = deque()
    q.append([begin,0])
    while q:
        n,turn = q.popleft()
        if n == target:
            answer = turn
            break
        for k in words:
            if similar(n,k) and [k,turn+1] not in q:
                q.append([k,turn +1]) 
    print(answer)
    return answer