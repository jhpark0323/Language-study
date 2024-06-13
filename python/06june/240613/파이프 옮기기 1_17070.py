from pprint import pprint

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
# pprint(arr)

# 방향, row, col
# 방향 ->
# 0 : 가로, 1 : 대각선, 2 : 세로
dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]
dp[0][0][0] = dp[0][1][0] = 1
# 각 ls의 0, 1, 2번째는 각각 전에서 가로, 대각선, 세로에서 왔다고 생각하면 됨
# pprint(dp)

for row in range(n):
    # 0열에서는 나올수가 없음
    for col in range(1, n):
        # 원래 파이프 형태가 가로
        if dp[row][col][0]:
            # 다음 위치가 가로의 형태
            # dp에 숫자가 있고 오른쪽 끝이 아니고 벽으로 안막혀 있으면
            if col < n-1 and not arr[row][col+1]:
                dp[row][col+1][0] += dp[row][col][0]
            # 다음 위치가 대각선의 형태
            if col < n-1 and row < n-1 and not arr[row][col+1] and not arr[row+1][col] and not arr[row+1][col+1]:
                dp[row+1][col+1][1] += dp[row][col][0]

        # 원래 파이프 형태가 대각선
        if dp[row][col][1]:
            # 다음 위치가 가로의 형태
            # dp에 숫자가 있고 오른쪽 끝이 아니고 벽으로 안막혀 있으면
            if col < n - 1 and not arr[row][col + 1]:
                dp[row][col + 1][0] += dp[row][col][1]
            # 다음 위치가 대각선의 형태
            if col < n - 1 and row < n - 1 and not arr[row][col + 1] and not arr[row + 1][col] and not arr[row + 1][col + 1]:
                dp[row + 1][col + 1][1] += dp[row][col][1]
            # 다음 위치가 세로의 형태
            if row < n-1 and not arr[row+1][col]:
                dp[row+1][col][2] += dp[row][col][1]

        # 원래 파이프 형태가 세로
        if dp[row][col][2]:
            # 다음 위치가 대각선의 형태
            if col < n - 1 and row < n - 1 and not arr[row][col + 1] and not arr[row + 1][col] and not arr[row + 1][col + 1]:
                dp[row + 1][col + 1][1] += dp[row][col][2]
            # 다음 위치가 세로의 형태
            if row < n-1 and not arr[row+1][col]:
                dp[row+1][col][2] += dp[row][col][2]

# pprint(dp)

print(sum(dp[-1][-1]))