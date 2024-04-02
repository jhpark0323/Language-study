arr = [list(map(int, input().split())) for _ in range(9)]
# print(arr)

row_ls = []

for row in range(9):
    row_ls.append(max(arr[row]))
# print(row_ls)

# print(max(row_ls))
# print(row_ls.index(max(row_ls)))

max_num = max(row_ls)

max_col = row_ls.index(max(row_ls))

max_row = arr[max_col].index(max_num)

print(max_num)
print(max_col+1, max_row+1)