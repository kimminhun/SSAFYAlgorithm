if __name__=="__main__":
    n,m=map(int,input().split())
    ar=sorted(list(input().split()))

    path=[]

    def dfs(idx):
        if len(path)==n:
            if validate():
                print(*path,sep='')
            return
        for i in range(idx,m):
            path.append(ar[i])
            dfs(i+1)
            path.pop()


    def validate():
        tmp = list('aeiou')
        acheck = 0
        bcheck = 0
        for x in path:
            if x in tmp:
                acheck += 1
            else:
                bcheck += 1
        if acheck >= 1 and bcheck >= 2:
            return True
        return False

    dfs(0)
