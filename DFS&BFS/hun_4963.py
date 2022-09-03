import sys

sys.setrecursionlimit(10000)

input = sys.stdin.readline


def dfs(x, y):
    visit[x][y]=True
    dx = [0, 0, -1, 1, 1, -1, 1, -1]
    dy = [1, -1, 0, 0, 1, 1, -1, -1]
    for i in range(8):
        cx = x + dx[i]
        cy = y + dy[i]
        if 0 <= cx < m and 0 <= cy < n and not visit[cx][cy] and ar[cx][cy] == 1:
            dfs(cx, cy)
    return 1


while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    ar = [list(map(int, input().split())) for _ in range(m)]
    visit = [[False] * n for _ in range(m)]
    cnt = 0
    for i in range(m):
        for j in range(n):
            if ar[i][j] == 1 and not visit[i][j]:
                cnt += dfs(i, j)

    print(cnt)
