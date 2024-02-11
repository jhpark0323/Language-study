# python으로는 시간초과, pypy3로는 통과

n, m = map(int, input().split())

# 0부터 n까지 만듬
graph = [[] for _ in range(n+1)]
# print(graph)

# graph 만들기
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# print(graph)

total_connected = []

def dfs(graph, start):
    visited = [False] * (n+1)
    visited[start] = True
    stack = [start]
    connected = []

    while stack:
        current_node = stack.pop()
        connected.append(current_node)
        for neighbor in graph[current_node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)
    return connected

for i in range(1, n+1):
    # print(dfs(graph, i))
    if set(dfs(graph, i)) not in total_connected:
        total_connected.append(set(dfs(graph, i)))

print(len(total_connected))