from collections import deque
import math
def solution(progresses, speeds):
    answer = []
    work_flow=deque() ## deque 선언
    for progres,speed in zip(progresses,speeds) : # 일해야할 일 수 계산  
        work_per = 100 - progres 
        work_day = math.ceil(work_per/speed)  ## math.ceil => 올림 3.5일 => 4일
        work_flow.append(work_day) 
    cnt=1 # 1개는 무적권 배포하니깐 1
    while(work_flow):
        if cnt > 1 : # 2개 이상 배포시 이미 배포된 부분 pop하면서 cnt를 1로 초기화
            cnt-=1 
            now_progres=work_flow.popleft()
            continue

        now_progres=work_flow.popleft() # 현재프로그레스 pop
        for progres in work_flow : 
            if now_progres >= progres : # 현재 프로그레스랑 비교해서 같거나 작으면 동시배포할거 찾음
                cnt+=1 
            else :  # 다음 프로그레스가 동시배포 안되면 그뒤는 볼필요 없음으로 break
                break
        answer.append(cnt) # 개수를 정답에 저장
    return answer