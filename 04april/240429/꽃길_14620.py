from pprint import pprint

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
pprint(arr)

# 일단 꽃술(중심)은 (1, 1) ~ (n-2, n-2)까지 가능
# for문 돌릴 때 range(1, n-1) 돌리기

def five_block(row, col):
    visited[row][col] = 1
    visited[row-1][col] = 1
    visited[row+1][col] = 1
    visited[row][col-1] = 1
    visited[row][col+1] = 1

    return arr[row][col] + arr[row-1][col] + arr[row+1][col] + arr[row][col-1] + arr[row][col+1]

min_val = float('inf')
for i in range(1, n-1):
    for j in range(1, n-1):
        # 씨앗 세개
        visited = [[0] * n for _ in range(n)]
        for k in range(3):
            # 방문 하지 않았다면
            if not visited[i][j]:
                val = five_block(i, j)
