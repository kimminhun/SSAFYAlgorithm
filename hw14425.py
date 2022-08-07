#  세트 교집합 개수 구하기 문제
# n, m = map(int, input().split())
# 입력 받기
# a= set()
# b= set()
# 빈 세트 두개 만들기
# for _ in range(n):
#     a.add(input())

# for _ in range(m):
#     b.add(input())
# c = a&b

# print(len(c))

#리스트를 통한 풀이
n, m = map(int, input().split())
a =[]
cnt = 0
for _ in range(n):
    a.append(input())
for _ in range(m):
    m = input()
    if m in a:
        cnt+= 1

print(cnt)


