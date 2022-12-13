def findboss(member):
    global arr
    if arr[member] == member:
        return member
    ret = findboss(arr[member])
    return ret

def union(a, b):
    global arr
    aboss=findboss(a)  # boss 찾기
    bboss=findboss(b)

    if aboss==bboss:  # boss가 같다 -> 이미 같은 그룹
        return
    if aboss < bboss:
        arr[bboss]=aboss
    else:
        arr[aboss]=bboss

def solution(n, computers):
    global arr
    arr = [i for i in range (n)]
    for i in range(n-1):
        for j in range(i+1, n):
            if computers[i][j] == 1:
                union(i, j)

    for i in range(n):
        arr[i] = findboss(i)

    return len(set(arr))


