from functools import cmp_to_key

def compare(x,y):
    if x+y <y+x:
        return 1
    else:
        return -1

def solution(numbers):
    answer = ''
    numbers=[str(num) for num in numbers]
    result=sorted(numbers,key=cmp_to_key(compare))
    
    return str(int(''.join(result)))