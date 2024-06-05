from heapq import heappush, heappop

# dijkstra 구현
# 시작지점을 for문으로 돌려가며 모든 점을 기준으로 시작해봄
# 각 시작지점에서 distance에 최소 경로를 넣고
# 최소경로가 수색범위 m 안에 들어있으면 갈수있는거

n, m, r = map(int, input().split())
item = list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
for i in range(r):
    a, b, l = map(int, input().split())
    graph[a].append([l, b])
    graph[b].append([l, a])

# 시작지점
def dijkstra(start):
    distance = [float('inf')] * (n+1)
    distance[start] = 0
    pq = []
    # 시작시 경로와, 점위치
    heappush(pq, [0, start])

    while pq:
        dist, now = heappop(pq)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            next_dist = dist + i[0]
            next_ = i[1]

            if distance[next_] > next_dist:
                distance[next_] = next_dist
                heappush(pq, [next_dist, next_])

    cnt = 0
    for i in range(n+1):
        # distance에서 거리가 m보다 작은 경우
        # -> 갈수있음
        if distance[i] <= m:
            # cnt에 그위치의 아이템 갯수를 더해줌
            cnt += item[i-1]

    return cnt

ans = 0
for start in range(1, n+1):
    new_ans = dijkstra(start)
    if ans < new_ans:
        ans = new_ans

print(ans)