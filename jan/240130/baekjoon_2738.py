n, m = map(int, input().split())

matrix_1 = [list(map(int, input().split())) for _ in range(n)]
matrix_2 = [list(map(int, input().split())) for _ in range(n)]

# print(matrix_1 + matrix_2)

# matrix_ans에 N x M인 0행렬을 만듬
matrix_ans = [[0 for _ in range(m)] for _ in range(n)]
# print(matrix_ans)

for row in range(n):
    for col in range(m):
        matrix_ans[row][col] = matrix_1[row][col] + matrix_2[row][col]
    print(*matrix_ans[row])