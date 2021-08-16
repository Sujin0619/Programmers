def solution(genres, plays):
    answer = []
    end = []
    dic = []
    type= []

    # 1. 장르 별로 정보 담기
    for i in range(len(genres)):
        temp = 0
        for j in range(len(type)):
            if genres[i]==type[j]:
                dic[j].append([i, plays[i]])
                dic[j][1]+=plays[i]
                temp=1
        if temp==0:
            type.append(genres[i])
            dic.append([genres[i], plays[i], [i, plays[i]]])

    dic.sort(key = lambda a:a[1], reverse=True) # 총 합으로 정렬하기
    print(dic)

    # 2. 곡 수만 빼내기
    for i in range(len(dic)):
        answer.append([])
        for j in range(2, len(dic[i])):
            answer[i].append(dic[i][j])

    for i in range(len(answer)):
        answer[i].sort(key = lambda  a: a[1], reverse=True) # 곡 수로 정렬하기

    print(answer)

    # 3. 각 장르에서 두 곡만 빼내기
    for i in range(len(answer)):
        if len(answer[i])==1:
            end.append(answer[i][0][0])
        else:
            end.append(answer[i][0][0])
            end.append(answer[i][1][0])

    print(end)


if __name__=='__main__':
    solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])