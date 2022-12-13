import sys

def find_boss(a):
    if boss_list[a] == a:
        return a
    else:
        ret = find_boss(boss_list[a])
        boss_list[a] = ret
        return ret

def union(a, b):
    fa, fb = find_boss(a), find_boss(b)
    if fa == fb:
        return 1
    else:
        boss_list[fb] = fa
        return 0

def minimum_cost(E):
    global cnt, sum_cost
    for i in range(E):
        if cnt == V:
            break
        a, b = arr[i][0]-1, arr[i][1]-1

        ret = union(a, b)
        if ret == 1:
            continue
        sum_cost += arr[i][2]
        cnt += 1

V, E = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(E)]
arr.sort(key = lambda x: x[2])
boss_list = [i for i in range(V)]
cnt = 0
sum_cost = 0

minimum_cost(E)
print(sum_cost)