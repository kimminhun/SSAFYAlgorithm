from itertools import combinations
n, k = map(int, input().split())
if k < 5:
    print(0)
else:
    k -= 5
    nece_chars = {'a', 'n', 't', 'i', 'c'}
    input_chars = []
    alpha = {ky: v for v, ky in enumerate(
        (set(map(chr, range(ord('a'), ord('z')+1))) - nece_chars))}
    cnt = 0
    for _ in range(n):
        tmp = 0
        for c in set(input())-nece_chars:
            tmp |= (1 << alpha[c])
        input_chars.append(tmp)
    power_by_2 = (2**i for i in range(21))
    for comb in combinations(power_by_2, k):
        test = sum(comb)

        ct = 0
        for cb in input_chars:
            if test & cb == cb:
                ct += 1

        cnt = max(cnt, ct)
    print(cnt)

# 아래는 set을 이용한 풀이지만 시간초과 나옴

# from itertools import combinations
# import copy
# import sys
# read = lambda : sys.stdin.readline().rstrip()
# n,k = map(int, input().split())
# li = []
# k -= 5
# def check(li):
#     cnt = 0
#     for i in li:
#         if len(i) == 0:
#             cnt +=1
#     return cnt
# for _ in range(n):
#     word = set(input())-{'a','n','t','i','c'}
#     li.append(word)
# if k <= 0:
#     print(check(li))
# else:
#     answer = 0
#     overlap_word = set()
#     for i in li:
#         overlap_word.update(i)
#     # overlap_word = list(overlap_word)
#     if len(overlap_word) <= k:
#         print(n)
#     else:
#         for j in combinations(overlap_word,k):
#            copy_li = copy.deepcopy(li)
#            for k in copy_li:
#                k -= set(j)
#            answer = max(check(copy_li), answer)
#         print(answer) 