import sys

n, m = map(int, sys.stdin.readline().split())
turn = []
for _ in range(m):
    turn.append(list(map(int, sys.stdin.readline().split())))

# print(turn)
arr = [-1]*n


def findboss(number):
    global arr
    if arr[number] == -1:
        return number
    ret = findboss(arr[number])
    arr[number] = ret
    return ret


# union 함수
def union(a, b):
    global arr

    fa, fb=findboss(a),findboss(b)
    if fa == fb:
        return 1
    if fa < fb:
        arr[fb] = fa
    else:
        arr[fa] = fb


answer = -1
for i in range(m):
    a, b = turn[i]
    ret = union(a, b)

    if ret == 1:
        answer = i
        break

print(answer+1)
