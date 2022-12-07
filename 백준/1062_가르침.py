

def dfs(level, idx):
    global max_cnt
    if level == K-5:
        tmp_cnt = 0
        for several in word_list:
            for i in several:
                if used[ord(i)-ord('a')] == 0:
                    break
            else:
                tmp_cnt += 1

        max_cnt = max(max_cnt, tmp_cnt)
        return

    for j in range(idx, 26):
        if used[j] == 0:
            used[j] = 1
            dfs(level+1, j)
            used[j] = 0



# print(used)
N, K = map(int, input().split())

word_list = []
for i in range(N):
    word = list(set(input()))
    word_list.append(word)
if K < 5:
    print(0)
    exit()
else:
    used = [0] * 26
    used[ord('a') - 97] = 1
    used[ord('n') - 97] = 1
    used[ord('t') - 97] = 1
    used[ord('i') - 97] = 1
    used[ord('c') - 97] = 1




# print(word_list)
    max_cnt = 0
    dfs(0,0)
    print(max_cnt)