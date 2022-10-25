def solution(tickets):
    answer = []
    tickets.sort(key=lambda x:(x[0],x[1]))
    visit=[False]*len(tickets)
    start="ICN"
    answer.append(start)

    def dfs(start,level):
        if level==len(tickets):
            return
        for i in range(len(tickets)):
            if tickets[i][0]==start and not visit[i]:
                visit[i]=True
                start=tickets[i][1]
                answer.append(start)
                dfs(start,level+1)

    dfs(start,0)
    return answer
# 재도전 필요
if __name__=="__main__":
    tickets=[['ICN','A'],['A','B'],['A','C'],['B','A'],['C','A']]
    print(solution(tickets))
