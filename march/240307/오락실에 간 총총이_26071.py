n = int(input())

arr = [list(input()) for _ in range(n)]
# print(arr)

ls = []
row_min = float('inf')
row_max = -float('inf')
col_min = float('inf')
col_max = -float('inf')
for i in range(n):
    for j in range(n):
        if 'G' == arr[i][j]:
            ls.append([i, j])
            if row_max < i:
                row_max = i
            if row_min > i:
                row_min = i
            if col_max < j:
                col_max = j
            if col_min > j:
                col_min = j

# print(ls)
# print('row_max :', row_max)
# print('row_min :', row_min)
# print('col_max :', col_max)
# print('col_min :', col_min)

if len(ls) == 1:
    print(0)
    exit()

answer = 0

if row_max == row_min:
    if n - 1 - col_max > col_min:
        answer += col_max
    else:
        answer += n - 1 - col_min
    print(answer)
    exit()

if col_max == col_min:
    if n - 1 - row_max > row_min:
        answer += row_max
    else:
        answer += n - 1 - row_min
    print(answer)
    exit()

# 어느쪽이 더 벽에 붙어 있는지 보고 그쪽으로 밈
# row_min이 더 벽에 붙음
if n-1 - row_max > row_min:
    answer += row_max
else:
    answer += n-1 - row_min

if n-1 - col_max > col_min:
    answer += col_max
else:
    answer += n-1 - col_min

print(answer)