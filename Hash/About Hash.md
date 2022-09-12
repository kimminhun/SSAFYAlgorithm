# <b>해시(Hash)란..?
<br>
<blockquote>키(key)와 값(value)쌍으로 이루어진 데이터 구조를 의미함. 파이썬에서는 딕셔너리(Dictionary) 타입이 해시와 같은 구조임.</blockquote>

<br>

## 해시의 장점

<ul> 데이터 저장/검색 속도가 빠름</ul>
<ul> 키에 대한 중복 확인이 쉬움.</ul>


## 해시의 단점

<ul> 일반적으로 저장공간이 좀 더 많이 필요함.</ul>


## 시간 복잡도
<ul>일반적인 경우: O(1)</ul>
<ul>최악의 경우: O(n)</ul>

<br>
<br>

# <b>파이썬 딕셔너리

### {키 : 값}
의 형태로 존재하는 자료형
<br>
순서가 없음(비시퀀스형 자료형)


## 딕셔너리 관련 함수
```python
dict = {'a':1, 'b':2}
dict.items() # 키, 값 쌍 추출 이 때 튜플 형태로 한 쌍식 리스트에 담겨 추출됨.
([('a',1), ('b',2)])

dict.get('a') # 1
dict.get('c') # None 값이 없을 때는 None반환
dict[c] #없는 key값으로 딕셔너리에 접근하면 에러가 나오므로 get을 더 많이 이용함

dict.del(key) #키값과 밸류값 한쌍을 지움

dict_1.fromkeys() #딕셔너리 생성 매서드
seq = ('name', 'age', 'sex')

dict_1 = dict.fromkeys(seq)
print(dict_1)

dict_2 = dict.fromkeys(seq, 10)
print(dict_2)

## result ##
{'age':None, 'name':None, 'sex':None}
{'age':10, 'name':10, 'sex':10}
```

참고사이트 :https://velog.io/@jaylnne/python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-dict.fromkeys-%EB%94%95%EC%85%94%EB%84%88%EB%A6%AC-%EC%83%9D%EC%84%B1-%EB%A9%94%EC%86%8C%EB%93%9C-%EC%A0%95%EB%A6%AC, https://davinci-ai.tistory.com/19
