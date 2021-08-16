def solution(m, n, puddles):
    n, m = m, n
    arr = [[0 for _ in range(m)] for _ in range(n)]

    for puddle in puddles:
        arr[puddle[0] - 1][puddle[1] - 1] = 'X'

    for i in range(1, m):
        if arr[0][i] == 'X':
            break
        arr[0][i] = 1

    for i in range(1, n):
        if arr[i][0] == 'X':
            break
        arr[i][0] = 1

    for i in range(1, n):
        for j in range(1, m):
            if arr[i][j] == 'X':
                continue
            elif arr[i - 1][j] == 'X' and arr[i][j - 1] == 'X':
                continue
            elif arr[i - 1][j] == 'X':
                arr[i][j] = arr[i][j - 1]
            elif arr[i][j-1] == 'X':
                arr[i][j] = arr[i - 1][j]
            else:
                arr[i][j] = arr[i - 1][j] + arr[i][j - 1]

    return (arr[n - 1][m - 1]) % 1000000007

if __name__=='__main__':
    print(solution(4, 3, [[2,2]]))