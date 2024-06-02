from heapq import heappush, heappop

start, end = map(int, input().split())

distance = [float('inf')] * 200001
distance[start] = 0
cnt = 0

def dijkstra():
    pq = []
    # count, 시작점
    heappush(pq, [0, start])

    while pq:
        count, current = heappop(pq)

        if distance[current] < count:
            continue

        # 3가지의 경우
        # 1번 (-1)
        next_count_1 = count+1
        next_1 = current-1

        if 0 <= next_1 <= 200000 and distance[next_1] > next_count_1:
            distance[next_1] = next_count_1
            heappush(pq, [next_count_1, next_1])

        # 2번 (*2)
        next_count_2 = count
        next_2 = current*2

        if 0 <= next_2 <= 200000 and distance[next_2] > next_count_2:
            distance[next_2] = next_count_2
            heappush(pq, [next_count_2, next_2])

        # 3번 (+1)
        next_count_3 = count+1
        next_3 = current+1

        if 0 <= next_3 <= 200000 and distance[next_3] > next_count_3:
            distance[next_3] = next_count_3
            heappush(pq, [next_count_3, next_3])

dijkstra()
# print(distance)
print(distance[end])
