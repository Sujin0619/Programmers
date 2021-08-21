import heapq


def solution(operations):
    min_heap = []
    for i in operations:
        instruction = i.split()[0]
        num = int(i.split()[1])

        if instruction == 'I':
            heapq.heappush(min_heap, num)

        elif instruction == "D":
            if len(min_heap) == 0:
                continue

            if num == -1:
                heapq.heappop(min_heap)

            else:
                max_heap = []
                for item in min_heap: # 최소힙 돌면서
                    heapq.heappush(max_heap, -item) # 음수로 넣기, 가장 큰 값이 음수가 되면 가장 앞으로 넣어짐

                for j in range(len(min_heap)):
                    if min_heap[j] == max_heap[0] * -1:
                        min_heap.pop(j)
                        break

    if len(min_heap) == 0:
        return [0, 0]

    else:
        max_heap = []
        for item in min_heap:
            heapq.heappush(max_heap, -item)

        return [max_heap[0] * -1, min_heap[0]]


if __name__ == '__main__':
    print(solution(["I 16","D 1"]))
