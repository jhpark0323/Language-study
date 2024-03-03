def dfs(row, col):
    # Base case: 마지막 row에 도달했을 경우
    if row == n - 1:
        return arr[row][col]

    # 이미 계산된 값을 사용
    # 같은 위치에 대한 계산 반복을 피함
    if memo[row][col] != -1:
        return memo[row][col]

    # 아래에서부터 최대합을 찾아서 올라옴
    memo[row][col] = arr[row][col] + max(dfs(row + 1, col), dfs(row + 1, col + 1))
    print(memo)
    return memo[row][col]

'''
5
7
3 8
8 1 0
2 7 4 4
400000000 5 2 6 5
'''

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# memoization을 위한 2D list 초기화
memo = [[-1] * n for _ in range(n)]

# (0, 0)에서 시작
max_sum = dfs(0, 0)
print(max_sum)