def balance(p):  # 균형잡힌 괄호 문자열의 개수를 리턴하는 함수
    left = 0
    right = 0

    for i in p:
        if i == '(':
            left += 1
        else:
            right += 1
        if left == right:
            return left + right  # 문자열 개수


def right(p):  # 올바른 괄호 문자열인지 확인하는 함수
    arr = []
    for i in p:
        if len(arr) == 0 and i == ')':
            return False
        if i == '(':
            arr.append(i)
        else:
            arr.pop()
    if len(arr) == 0:
        return True


def trans(p):
    # 1번
    if len(p) == 0:
        return ""

    # 2번
    balanced_num = balance(p)
    u = p[:balanced_num]  # )(
    v = p[balanced_num:]  # ""

    # 3번
    if right(u):
        return u + trans(v)

    # 4번
    else:
        empty = '('
        empty += trans(v)
        empty += ')'
        string = u[1:-1]
        for i in string:
            if i == '(':
                empty += ')'
            else:
                empty += '('
        return empty


def solution(p):
    answer = trans(p)
    return answer


print(solution(')('))