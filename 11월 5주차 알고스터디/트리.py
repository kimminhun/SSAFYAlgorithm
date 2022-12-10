import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
delete_node = int(input())
def dfs(num, li):
    li[num] = -2
    for i in range(len(li)):
        if li[i] == num:
            dfs(i,li)

dfs(delete_node, li)
count = 0
for i in range(len(li)):
    if li[i] != -2 and i not in li:
        count += 1
print(count)

