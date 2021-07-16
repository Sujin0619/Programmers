from itertools import permutations

def decimal(num):  # 소수인지 아닌지 판별해주는 함수
    if num == 1 or num == 0:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    length = len(numbers)
    duplicate_check = []

    for i in range(1, length + 1):
        arr = list(permutations(numbers, i))
        for temp in arr:
            word = ""
            for j in range(len(temp)):
                word += temp[j]
            if decimal(int(word)):
                duplicate_check.append(int(word))
    answer = len(set(duplicate_check))
    return answer