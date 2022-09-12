# l 개의 알파벳 으로 구성된 C개 중 조합
l, c = map(int, input().split())
li = list(input().split())
li.sort()
word=['']*l
def dfs(start, level):
    global word
    if level == l:
        if  l -2 >= word.count('a')+word.count('e') +word.count('i') +word.count('o') + word.count('u') > 0:
            print(*word, sep = '')
        return

    for i in range(start, c):
        if li[i] not in word:
            word[level] = li[i]
            dfs(i, level+1)
            word[level] = ''
dfs(0,0)