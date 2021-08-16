def solution(money):
    if len(money) == 3:
        return max(money)

    dp0 = []
    dp1 = []

    # 초기화
    dp0.append(money[0])
    dp1.append(0)

    dp0.append(0)
    dp1.append(money[1])

    dp0.append(money[0] + money[2])
    dp1.append(0)

    for i in range(3, len(money)):
        dp0.append(money[i] + max(dp0[i - 2], dp0[i - 3]))
        dp1.append(money[i] + max(dp1[i - 2], dp1[i - 3]))

    dp0[-1] -= money[0]

    return max(max(dp0), max(dp1))

if __name__=='__main__':
    print(solution([1, 2, 3, 1]), 4)
    print(solution([1, 1, 4, 1, 4]), 8)
    print(solution([1000, 0, 0, 1000, 0, 0, 1000, 0, 0, 1000]), 3000)
    print(solution([1000, 1, 0, 1, 2, 1000, 0]), 2001)
    print(solution([1000, 0, 0, 0, 0, 1000, 0, 0, 0, 0, 0, 1000]), 2000)
    print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 30)
    print(solution([0, 0, 0, 0, 100, 0, 0, 100, 0, 0, 1, 1]), 201)
    print(solution([11, 0, 2, 5, 100, 100, 85, 1]), 198)
    print(solution([1, 2, 3]), 3)
    print(solution([91, 90, 5, 7, 5, 7]), 104)
    print(solution([90, 0, 0, 95, 1, 1]), 185)