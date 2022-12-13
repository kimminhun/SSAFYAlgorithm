from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    for num in course:
        tmp = []
        for order in orders:
            order = sorted(order)
            tmp.extend(list(combinations(order, num)))

        # 조합의 중복횟수 세기
        duple = Counter(tmp)

        if duple:
            # 조합이 최소 2번 이상 구성되어야함
            if max(duple.values()) >= 2:
                print(duple)
                for key, value in duple.items():
                    if value == max(duple.values()):
                        answer.append("".join(key))
    return sorted(answer)


