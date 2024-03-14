from collections import deque

def bfs(start):
    visited = [False] * len(graph)
    visited[start] = True
    cnt = 0
    q = deque([[start, cnt]])

    while q:
        current, cnt = q.popleft()
        for neighbor in graph[current]:
            if not visited[neighbor]:
                q.append([neighbor, cnt+1])
                visited[neighbor] = True
                count.append(cnt+1)

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(m)]

graph = [[] for _ in range(n+1)]

for i in arr:
    graph[i[0]].append(i[1])
    graph[i[1]].append(i[0])
# print(graph)

# answer = []
ans = float('inf')
low_person = 0
for i in range(1, n+1):
    count = []
    bfs(i)
    new_ans = sum(count)
    # answer.append([i, sum(count)])

    if ans > new_ans:
        ans = new_ans
        low_person = i

# print(answer)
print(low_person)