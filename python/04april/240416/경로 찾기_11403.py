import sys
from pprint import pprint

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def dfs(start):
    visited = [False] * (n+1)
    stack = [start]
    # 방문한 곳 담을 ls
    ls = []

    while stack:
        current = stack.pop()
        # print(current)

        for neighbor in range(n):
            if arr[current][neighbor] and not visited[neighbor]:
                stack.append(neighbor)
                ls.append(neighbor)
                visited[neighbor] = True

    return ls

# new_ls = dfs(1)
# print(new_ls)

ans = [[0]*(n) for _ in range(n)]


for i in range(n):
    new_ls = dfs(i)
    for j in new_ls:
        ans[i][j] = 1

# pprint(ans)

for i in ans:
    print(*i)