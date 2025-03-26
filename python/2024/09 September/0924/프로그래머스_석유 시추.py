from collections import deque


def solution(land):
    n = len(land)
    m = len(land[0])
    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]
    answer = 0

    result = [0 for _ in range(m + 1)]

    def bfs(i, j):
        visited[i][j] = True
        q = deque([[i, j]])
        ans = 1
        min_j = max_j = j
        while q:
            cur_r, cur_c = q.popleft()
            min_j = min(min_j, cur_c)
            max_j = max(max_j, cur_c)

            for dij in range(4):
                next_r = cur_r + di[dij]
                next_c = cur_c + dj[dij]

                if 0 <= next_r < n and 0 <= next_c < m and not visited[next_r][next_c] and land[next_r][next_c]:
                    ans += 1
                    q.append([next_r, next_c])
                    visited[next_r][next_c] = True

        for col in range(min_j, max_j + 1):
            result[col] += ans

    visited = [[False] * m for _ in range(n)]
    for i in range(m):
        for j in range(n):
            if land[j][i] and not visited[j][i]:
                bfs(j, i)

    answer = max(result)

    return answer

