# n = int(input())
# a= {} #들어오는 차 딕셔너리 
# b= {} #나가는 차 딕셔너리
# car_list= [] # 차 번호 리스트
# cnt= 0
# for i in range(n): # 들어오는 차 딕셔너리, 리스트에 넣음
#     car = input()
#     a[car] = i 
#     car_list.append(car)

# for x in range(n): # 나가는 차 딕셔너리에 넣음
#     b[input()] = x

# for n in car_list: # 차번호 순회 돌면서 밸류값 비교
#     if a[n] > b[n]:
#         cnt+=1
# print(cnt)
#------위 코드는 매력적인 오답임-----------

n = int(input())

car_in_dict = {}
car_out_list= []
cnt = 0
for i in range(1, n+1):
    car_in_dict[input()] = i
for x in range(n):
    car_out_list.append(car_in_dict[input()]) 
for r in range(n-1):
    for s in range(r+1, n):
        if car_out_list[r] > car_out_list[s]:
            cnt +=1
            break
print(cnt)



