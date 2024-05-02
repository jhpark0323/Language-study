from collections import deque

'''
백트래킹으로 다시 풀어보기
'''

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]


def dfs(row, col):
    visited = [[0] * c for _ in range(r)]
    visited[row][col] = 1
    # 행, 열, 거리, 지나온 길
    q = deque([[row, col, 1, []]])
    ans = 0
    passed_ls = []

    while q:
        current_row, current_col, count, ls = q.popleft()
        visited[current_row][current_col] = 1
        print('current_row :', current_row)
        print('current_col :', current_col)
        print('count :', count)
        print()


        # 거리가 k, 집에도착 하였을 때, 지나온길이 없을 때
        if count == k and current_row == home_r and current_col == home_c and ls not in passed_ls:
            ans += 1
            passed_ls.append(ls)
            print(ans)
            # visited = [[0] * c for _ in range(r)]
            # visited[row][col] = 1
            continue

        # 거리가 k이상이면 그냥 넘김
        elif count >= k:
            # visited = [[0] * c for _ in range(r)]
            # visited[row][col] = 1
            continue

        for dij in range(4):
            next_r = current_row + di[dij]
            next_c = current_col + dj[dij]
            # 범위안에있고 '.'이고 방문하지 않았으면
            if 0 <= next_r < r and 0 <= next_c < c and arr[next_r][next_c] == '.' and not visited[next_r][next_c]:
            # if 0 <= next_r < r and 0 <= next_c < c and arr[next_r][next_c] == '.':
                ls.append([next_r, next_c])
                q.append([next_r, next_c, count+1, ls])

    print(passed_ls)
    return ans


r, c, k = map(int, input().split())
arr = [list(input()) for _ in range(r)]
# print(arr)

# 시작점, 집
start_r, start_c = r-1, 0
home_r, home_c = 0, c-1

print(dfs(start_r, start_c))