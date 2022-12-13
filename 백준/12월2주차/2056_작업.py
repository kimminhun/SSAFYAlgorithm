N = int(input())
arr = [[] for _ in range(N)]
time = [0]*N

for i in range(N):
    lst = list(map(int, input().split()))
    time[i] = lst[0]
    if lst[1] > 0:
        for j in range(lst[1]):
            arr[i].append(lst[2+j])
# print(arr)

for i in range(N):
    temp = 0
    if len(arr[i]) > 0:
        for j in arr[i]:
            temp = max(temp, time[j-1])
        time[i] += temp
print(max(time))
