# 트리의 부모 찾기
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
n = int(input())
arr = [[0]*n for _ in range(n)]
ans = [0]*n
used= [0]*n
for _ in range(n-1):
    i, j = map(int, input().split())
    arr[i-1][j-1] = 1
    arr[j-1][i-1] = 1
print(arr)
def dfs(now,mom):
    global ans
    ans[now] = mom+1
    for x in range(7):
        if arr[now][x] == 1 and used[x] != 1:
            used[x] = 1
            dfs(x,now)
used[0] = 1
dfs(0,0)
for x in ans[1:]:
    print(x)