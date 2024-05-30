from collections import deque
from itertools import combinations


def bfs(arr):
    global people, graph
    start = arr[0]
    queue = deque([start])
    visited = set([start])
    num = 0

    while queue:
        value = queue.popleft()
        num += people[value]
        for i in graph[value]:
            # 방문하지 않았고 arr에 있으면
            if i not in visited and i in arr:
                queue.append(i)
                visited.add(i)
    return num, len(visited)


N = int(input())
people = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]

for i in range(1, N + 1):
    graph[i] = list(map(int, input().split()))
    graph[i] = graph[i][1:]
# print(graph)

result = float('inf')
for i in range(1, N // 2 + 1):
    combis = list(combinations(range(1, N + 1), i))
    for combi in combis:
        sum1, node1 = bfs(combi)
        # combi에 없는 것들을 다시 돌려봄
        sum2, node2 = bfs([i for i in range(1, N + 1) if i not in combi])
        # 두 선거구의 모든 노드가 연결되어 있는지 확인
        if node1 + node2 == N:
            result = min(result, abs(sum1 - sum2))

if result != float('inf'):
    print(result)
else:
    print(-1)