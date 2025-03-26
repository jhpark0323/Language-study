import sys
from collections import deque

input = sys.stdin.readline

# bfs를 w를 시작으로 하여 돈다
# w건물을 짓기위해 필요한 건물들을 차례로 순회
# bfs기 때문에 for문이 끝날 시 그 회차?에 필요한 건물들이 나열 될 것
# 그것들 끼리 비교해서 제일 큰 값을 ans에 더해줌
def bfs():
    visited = [False] * (k+1)
    # 시작점 w
    visited[w] = True
    q = deque([w])

    # 처음 시작은 w를 건설하는데 걸리는 시간으로 잡음
    ans = dn[w-1]

    while q:
        current = q.popleft()

        for neighbor in graph[current]:
            max_time = 0
            if not visited[neighbor]:
                q.append(neighbor)
                visited[neighbor] = True
                # for문 돌때 그 건물을 짓기 위해 필요한 모든 건물들을 다 순회 할 것이기에
                # 그중에서 제일 큰 값을 구한다
                max_time = max(max_time, dn[neighbor-1])

        # for문이 끝나면 max_time에 저장된 값을 더해준다
        ans += max_time

    return ans


T = int(input())

for _ in range(T):
    n, k = map(int, input().split())
    dn = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(k)]
    w = int(input())
    # print(n, k)
    # print(dn)
    # print(arr)
    # print(w)

    # graph[i]에는 i번째 건물을 짓기 위해 필요한 건물들을 append
    # ex 1번 test_case :
    # [[], [], [1], [1], [2, 3]]
    graph = [[] for _ in range(k+1)]
    # print(graph)
    for i in arr:
        graph[i[1]].append(i[0])

    # print(graph)

    print(bfs())