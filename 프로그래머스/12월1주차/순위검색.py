from itertools import combinations

# 효율성 통과를 위해 조합, 이분탐색을 사용해야 하는 문제!
def solution(info, query):
    answer = []
    info_dict = {}

    for i in range(len(info)):
        info1 = info[i].split()
        # 조건은 key, 점수는 value 로 분류
        key = info1[:-1]
        val = info1[-1]

        # key들로 만들 수 있는 모든 조합 생성
        for j in range(5):
            for c in combinations(key, j):
                tmp = ''.join(c)
                if tmp in info_dict:
                    info_dict[tmp].append(int(val))
                else:
                    info_dict[tmp] = [int(val)]


    for i in info_dict:
        info_dict[i].sort()

    # 조건은 key, 점수는 value 로 분류
    for qu in query:
        qu1 = qu.split(' ')
        qu_key = qu1[:-1]
        qu_val = qu1[-1]

        while 'and' in qu_key:
            qu_key.remove('and')
        while '-' in qu_key:
            qu_key.remove('-')
        qu_key = ''.join(qu_key)

        # qu_key에 해당하는 info_dict의 점수를 scores로 받아옴
        if qu_key in info_dict:
            scores = info_dict[qu_key]

            # 이분탐색으로 query 조건을 만족하는 score의 갯수 구하기
            left = 0
            right = len(scores) - 1

            while left <= right:
                mid = (left + right) // 2

                if int(qu_val) > scores[mid]:
                    left = mid + 1
                elif int(qu_val) <= scores[mid]:
                    right = mid - 1

            answer.append(len(scores) - left)
        else:
            answer.append(0)

    return answer
