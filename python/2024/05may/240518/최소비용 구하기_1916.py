n = int(input())
m = int(input())
arr = [list(map(int, input().split())) for _ in range(m)]
start, end = map(int, input().split())

graph = [[] for _ in range(n+1)]
# print(graph)

for i in range(m):
    start_city = arr[i][0]
    end_city = arr[i][1]
    cost = arr[i][2]

    graph[start_city].append([end_city, cost])

print(graph)

