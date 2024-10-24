from pprint import pprint

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

cctv = []
for i in range(n):
    for j in range(m):
        if arr[i][j] != 0 and arr[i][j] != 6:
            cctv.append([i, j])

cctv_num = len(cctv)

# 1 : 북, 2 : 동, 3 : 남, 4 : 서
dir = [
    [],
    [[1], [2], [3], [4]],
    [[1, 3], [2, 4]],
    [[1, 2], [2, 3], [3, 4], [4, 1]],
    [[1, 2, 3], [2, 3, 4], [3, 4, 1], [4, 1, 2]],
    [[1, 2, 3, 4]]
]

ans = 1e9

def count_blind_spot():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                cnt += 1
    return cnt

def change_view(row, col, directions, change):
    modified = []
    for direction in directions:
        new_row, new_col = row, col
        while True:
            if direction == 1:
                new_row -= 1
            elif direction == 2:
                new_col += 1
            elif direction == 3:
                new_row += 1
            elif direction == 4:
                new_col -= 1

            if not (0 <= new_row < n and 0 <= new_col < m):
                break

            if arr[new_row][new_col] == 6:
                break

            if arr[new_row][new_col] == 0:
                arr[new_row][new_col] = change
                modified.append((new_row, new_col))

    return modified

def back(cnt):
    global ans
    if cnt == cctv_num:
        new_ans = count_blind_spot()
        ans = min(new_ans, ans)
        # pprint(arr)
        return

    this_turn = cctv[cnt]
    cctv_number = arr[this_turn[0]][this_turn[1]]

    for directions in dir[cctv_number]:
        modified = change_view(this_turn[0], this_turn[1], directions, '#')
        back(cnt + 1)
        for (r, c) in modified:
            arr[r][c] = 0

back(0)
print(ans)
