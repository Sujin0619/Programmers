def dfs(tickets, answer, visited):
    if sum(visited) == len(tickets):
        # 모두 방문했다면
        return 1 # else문 if문에서 끝남

    if len(answer) == 0:
        # ICN 찾기
        for i in range(len(tickets)):
            if tickets[i][0] == 'ICN':
                visited[i] = 1
                answer.append('ICN')
                answer.append(tickets[i][1])  # 도착지(이자 출발지) 넣기
                if dfs(tickets, answer, visited):
                    return
                # 안 끝나는 경우
                visited[i] = 0
                answer.pop()
                answer.pop() # ICN까지 빼야함

    else:
        for i in range(len(tickets)):
            if visited[i] == 0 and answer[-1] == tickets[i][0]:  # 도착지가 출발지인 경우
                visited[i] = 1
                answer.append(tickets[i][1])  # 출발지 넣기
                if dfs(tickets, answer, visited):
                    return 1 # 정답 찾으면 윗단계 if문에서 return으로 끝남
                # 안 끝나는 경우
                visited[i] = 0
                answer.pop()


def solution(tickets):
    answer = []
    visited = [0 for _ in range(len(tickets))]
    # 티켓을 사용했는지 안사용했는지 파악하기 위해

    tickets.sort(key=lambda temp: temp[0])
    tickets.sort(key=lambda temp: temp[1])

    print(tickets)
    dfs(tickets, answer, visited)

    print(answer)

def main():
    solution([["ICN", "COO"], ["ICN", "BOO"], ["COO", "ICN"], ["BOO", "DOO"]])
    # 답은 ["ICN", "COO", "ICN", "BOO", "DOO"]

if __name__=='__main__':
    main()