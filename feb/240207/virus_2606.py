def dfs(graph, start):
    # 방문한 행렬을 표시할 visited list 생성
    visited = [False] * len(graph)
    # stack에 시작할 곳 append
    stack = [start]
    # 시작했으므로 visited의 start를 True로 바꿈
    visited[start] = True
    # 세어줄 변수
    count = 0

    # stack안에 원소가 없을 때 까지
    while stack:
        # 현재노드 = stack의 마지막 원소 -> pop
        current_node = stack.pop()
        # pop하면서 횟수 세기
        count += 1
        # 현재노드로 갈 수 있는 곳들을 순회 -> graph에 있음
        for neighbor in graph[current_node]:
            # neighbor가 아직 방문하지 않은 곳이면
            if not visited[neighbor]:
                # stack에 neighbor append
                stack.append(neighbor)
                # 그 후 True로 교체
                visited[neighbor] = True

    # 시작노드는 제외
    return count -1

# 컴퓨터의 수
N = int(input())
# 직접 연결된 쌍의 수
M = int(input())

# index를 간편하게 쓰기 위해서 N+1개 생성
graph = [[] for _ in range(N+1)]

# 직접 연결된 만큼 반복
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(dfs(graph, 1))