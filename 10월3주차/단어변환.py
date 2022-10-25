def solution(begin, target, words):
    answer = 0
    visit=[False]*len(words)
    result=[]

    if target not in words:
        return answer

    def dfs(word,level):
        if word==target:
            result.append(level)
            return

        for i in range(len(words)):
            if not visit[i]:
                tmp=words[i]
                cnt=0
                for j in range(len(word)):
                    if tmp[j]!=word[j]:
                        cnt+=1
                if cnt==1:
                    visit[i]=True
                    dfs(tmp,level+1)
                    visit[i]=False

    dfs(begin,0)
    answer=min(result)
    return answer