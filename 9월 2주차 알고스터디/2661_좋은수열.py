min_num = 21e8
n = int(input())
def dfs(level,arr):
    global min_num
    if level > 2:
        if good(arr):
            return
    if level == n-1:
        if int(arr) < min_num:
            min_num = int(arr)
        return
    for  i in range(1,4):
        if  int(arr[-1]) != i:
            dfs(level+1,arr+str(i))

def good(arr):
    flag = 1
    for tum in range(1,len(arr)//2):
        if flag == 0:
            break
        for start in range((len(arr)-tum*2)+1):
            if arr[start:start+tum] == arr[start+tum:start+tum+tum]:
                flag = 0
                break
    if flag == 1:
        return False
    else: return True
for start_num in range(1,4):
    dfs(0,f'{start_num}')

print(min_num)
