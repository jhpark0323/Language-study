import sys

input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
# print(arr)

di = [0, 1]
dj = [1, 0]

dp = [[0] * n for _ in range(n)]
dp[0][0] = 1
# print(dp)
for row in range(n):
    for col in range(n):
        # 맨마지막(도착지점)은 실행하지 않는다
        # -> 맨마지막은 arr이 0이라서 두방향이 그냥 더해짐
        if dp[row][col] and not (row == n-1 and col == n-1):
            # print('row :', row)
            # print('col :', col)
            # 두개의 방향을 생각
            for i in range(2):
                next_row = row + di[i] * arr[row][col]
                next_col = col + dj[i] * arr[row][col]

                if 0 <= next_row < n and 0 <= next_col < n:
                    dp[next_row][next_col] += dp[row][col]

            # print(dp)

# print(dp)
print(dp[-1][-1])
