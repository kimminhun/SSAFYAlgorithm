from itertools import combinations
def solution(brown, yellow):
    answer = []
    # 가로
    li = []
    for i in range(1,yellow+1):
        if yellow%i == 0:
            li.append([yellow//i,i])
    for j in range(len(li)//2+1):
        print(li[j])
        if (li[j][0]+2)*2 + li[j][1]*2 == brown:
            answer.append(li[j][0]+2)
            answer.append(li[j][1]+2)
            break
    return answer