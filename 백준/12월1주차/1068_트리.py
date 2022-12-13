# arr 안에 index와 같은 원소가 있다면 리프노드가 아님.

N = int(input())
arr = list(map(int, input().split()))
target = int(input())


def dfs(x):
    arr[x] = -2
    for i in range(N):
        if x == arr[i]:
            dfs(i)



dfs(target)
cnt = 0
for i in range(N):
    if arr[i] != -2:
        if i not in arr:
            cnt += 1

print(cnt)
