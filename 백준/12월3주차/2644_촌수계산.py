import sys
n = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())

# 부모 노드를 기록할 리스트
lst = [0]*(n+1)

for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    # arr.append([x, y])
    lst[y] = x
# print(lst)


def dfs(p):
    global parent_lst
    if lst[p] == 0:
        return
    parent_lst.append(lst[p])
    dfs(lst[p])

# dfs를 돌며 parent_lst에 부모노드 값을 추가
parent_lst = []
dfs(a)
result1 = parent_lst

parent_lst = []
dfs(b)
result2 = parent_lst

# print(result1, result2)

answer = -1
flag = 0

# a가 b의 직계 후손인 경우
if a in result2:
    answer = result2.index(a)+1

# b가 a의 직계 후손인 경우
elif b in result1:
    answer = result1.index(b)+1

# a와 b의 조상이 같은경우
else:
    for i in range(len(result1)):
        for j in range(len(result2)):
            if result1[i] == result2[j]:
                answer = i+j+2
                flag = 1
                break
        if flag == 1:
            break
# 위의 3가지 경우가 아니면 a와 b의 촌수를 계산할 수 없음.
print(answer)

