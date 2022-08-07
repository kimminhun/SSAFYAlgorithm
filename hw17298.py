import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
lis = list(map(int, input().split()))
result = [-1]*n
st = deque()

for i in range(n):
    while st:
        if lis[i] > lis[st[-1]]:
            result[st.pop()]=lis[i]
        else:
            break
    st.append(i)


# without Stack
# n = int(sys.stdin.readline())
# arr = list(map(int, sys.stdin.readline().split()))
# for x in range(0,n):
#     if x == n-1:
#         print(-1)
#     for y in range(x+1,n):
#         if arr[y] > arr[x]:
#             print(arr[y], end =' ')
#             break
#         elif max(arr[x:]) == arr[x]:
#             print(-1, end =' ')
#             break