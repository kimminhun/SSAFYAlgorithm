n, m = map(int, input().split())
def dfs(arr,level):
    if len(arr) >= 2 and arr[-1] < arr[-2]:
        return
    if level == m:
        print(*arr, sep=' ')
        return

    for i in range(1,n+1):
        arr.append(i)
        dfs(arr,level+1)
        arr.pop()
dfs([],0)

# dfs 함수에 빈 리스트를 넣어도 정상적으로 작동 함







