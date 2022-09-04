from collections import deque
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
def bfs(y,x):
    queue = deque()
    queue.append((y,x))
    while queue:
        y,x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<= nx < m and 0<= ny < n and graph[ny][nx] == 1:
                graph[ny][nx] = graph[y][x] +1
                queue.append((ny,nx))
    return graph[n-1][m-1]
print(bfs(0,0))