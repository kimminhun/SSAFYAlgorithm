import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

num = n/2
used = [0]*n
min_valance = 21e8


def abc(level,idx):
    global  min_valance
    if min_valance == 0:
        print(0)
        exit(0)
    if level==(num):
        a_score, b_score =0,0
        for y in range(n):
            for x in range(n):
                if used[y] == 1 and used[x] == 1:
                    a_score += arr[y][x]
                elif used[y] == 0 and used[x] ==0:
                    b_score += arr[y][x]
        valance = abs(a_score - b_score)
        if valance < min_valance:
            min_valance = valance
        return    


    for i in range(idx,n):
        if used[i] ==0:
            used[i] = 1
            abc(level+1,i)
            used[i]=0




abc(0,0)  #level start
print(min_valance)