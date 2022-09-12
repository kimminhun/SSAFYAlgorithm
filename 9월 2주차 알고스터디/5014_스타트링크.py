from collections import deque

f,start,goal,up,down = map(int,input().split())
ans = [0]*(f+1)
q = deque()
q.append(start)
ans[start] = 1
while q:
    if ans[goal] != 0:
        break
    now = q.popleft()
    if (now + up) <= f and ans[now+up] == 0:
        ans[now+up] = ans[now]+1
        q.append(now+up)
    if now - down > 0 and ans[now-down] == 0:
        ans[now-down] = ans[now]+1
        q.append(now-down)
if ans[goal] == 0:
    print('use the stairs')
else:
    print(ans[goal]-1)
        
