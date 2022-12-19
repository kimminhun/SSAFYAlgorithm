from collections import deque

S = int(input())
def bfs(S):
    global time
    q = deque()
    q.append((1,0,0))
    used = [[0]*1001 for _ in range(1001)]

    while q:
        count, board, time = q.popleft()
        used[1][0] = 1
        if count == S:
            break
        for i in range(3):
            if i == 0:
                new_count, new_board, new_time = count, count, time+1

            elif i == 1:
                new_count, new_board, new_time = count+board, board, time+1

            else:
                new_count, new_board, new_time = count-1, board, time+1

            if new_count >= 1001 or new_count < 0 or new_board >= 1001 or new_board < 0: continue
            if used[new_count][new_board] == 1: continue
            used[new_count][new_board] = 1
            q.append((new_count, new_board, new_time))

    return time

print(bfs(S))