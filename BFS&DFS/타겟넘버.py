# 프로그래머스 타겟 넘버


def solution(numbers, target):
    answer = 0
    def dfs(level, now):
        nonlocal answer
        pm = [-1,1]
        if level == len(numbers):
            if now == target:
                answer += 1
            return
        for i in range(2):
            dfs(level+1,now + pm[i]*numbers[level])
    dfs(0,0)
    
    return answer
