
n, m =map(int, input().split())
dict = {}
for i in range(n): # 걸그룹 팀이름, 팀원이름 받아서 딕셔너리에 넣기
    name_lis = []
    team = input()# 팀 이름
    dgr = int(input())#팀 인원
    for x in range(dgr):
        name = input()
        name_lis.append(name)
        #이름 리스트에 팀원 이름 넣기
    name_lis.sort()
    #이름 사전순 정렬
    dict[team] = name_lis
for q in range(m):# 퀴즈 받기
    q_name = input()
    qtype = int(input())
    if qtype == 0:# 팀원 이름 출력
        for r in dict[q_name]:
            print(r)
    for k in dict.keys():# 팀명 출력
        if q_name in dict[k]:
            print(k)
    




    

    

