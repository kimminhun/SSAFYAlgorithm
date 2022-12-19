import sys

N, M = map(int, sys.stdin.readline().split())
# M과 Tk의 최댓값이 각각 10^9 이므로 시간의 최댓값은 10^18
result = 10e18
lst = []
for _ in range(N):
    lst.append(int(sys.stdin.readline()))


left, right = 1, M*max(lst)


while left <= right:
    mid = (left+right)//2
    tmp_result = 0
    for i in range(N):
        tmp_result += (mid // lst[i])
    if tmp_result >= M:
        result = min(result, mid)
        right = mid - 1
    else:
        left = mid + 1

print(result)

