from collections import deque

def dfs(v):
    visited = [False] * (n+1)
    visited[v] = True
    stack = [v]
    ls = []

    while stack:
        current = stack.pop()
        visited[current] = True
        # dfs는 뒤에서 부터 빼기 때문에 내림차순으로 정렬한 후 순회
        graph[current].sort(reverse = True)
        if current not in ls:
            ls.append(current)
        for neighbor in graph[current]:
            if not visited[neighbor]:
                stack.append(neighbor)
                # ls.append(neighbor)
                # print('ls :', ls)
                # print('stack :', stack)
    return ls

def bfs(v):
    visited = [False] * (n+1)
    visited[v] = True
    q = deque([v])
    ls = []

    while q:
        current = q.popleft()
        visited[current] = True
        # bfs는 앞에서 부터 빼기 때문에 오름차순으로 정렬한 후 순회
        graph[current].sort()
        if current not in ls:
            ls.append(current)
        for neighbor in graph[current]:
            if not visited[neighbor]:
                q.append(neighbor)
                # ls.append(neighbor)
                # print('ls :', ls)
                # print('stack :', stack)
    return ls

# n : 정점의 갯수, m : 간선의 갯수, v : 탐색시작
n, m, v = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]

graph = [[] for _ in range(n+1)]
for i in arr:
    start, end = i[0], i[1]
    graph[start].append(end)
    graph[end].append(start)
# print(graph)

answer_dfs = dfs(v)
print(*answer_dfs)
answer_bfs = bfs(v)
print(*answer_bfs)