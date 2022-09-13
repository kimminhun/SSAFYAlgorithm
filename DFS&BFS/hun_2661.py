import sys
input=sys.stdin.readline

def check(st):
    for i in range(len(st)):
        tmp=st[i:]
        for j in range(1,len(tmp)//2+1):
            checktmp=tmp[:j]
            if checktmp==tmp[j:j+j]:
                return False
    return True

def dfs(now):
    if not check(st):
        return -1
    if now==n:
        print(*st,sep="")
        return 0

    for i in range(1,4):
        st.append(i)
        if dfs(now+1)==0:
            return 0
        st.pop()

if __name__=="__main__":
    n=int(input())
    st=[]
    dfs(0)