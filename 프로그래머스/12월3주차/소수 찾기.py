from itertools import permutations
def primenumber(x):
    if x <= 1:
        return 0
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return 0
    return 1

def solution(numbers):

    permutation = []
    result_list = []
    answer = 0
    for i in range(1, len(numbers)+1):
        permutation.append(list(permutations(numbers, i)))
    for i in range(len(permutation)):
        for j in range(len(permutation[i])):
            result_list.append(''.join(permutation[i][j]))
    result_list = list(set(list(map(int, set(result_list)))))

    for i in range(len(result_list)):
        tmp = primenumber(result_list[i])
        if tmp == 1:
            answer += 1
    return answer








