def solution(triangle):
    n = len(triangle)
    arr = [[] for _ in range(n)]  # 미리 크기만큼 배열 두기

    arr[0].append(triangle[0][0])

    for i in range(1, n):  # 1층부터 돌기
        for j in range(len(triangle[i])):  # 층마다 열돌기
            if j == 0:
                arr[i].append(arr[i - 1][0] + triangle[i][j])
            elif j == len(triangle[i]) - 1:
                arr[i].append(arr[i - 1][-1] + triangle[i][j])
            else:
                a, b = arr[i - 1][j - 1], arr[i - 1][j]
                arr[i].append(max(a, b) + triangle[i][j])

    return max(arr[-1])

if __name__=="__main__":
    print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))