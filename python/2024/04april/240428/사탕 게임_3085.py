from pprint import pprint
from copy import deepcopy
n = int(input())
arr = [list(input()) for _ in range(n)]
# pprint(arr)

def count_longest(array):
    max_count = 0
    # 1부터 마지막까지 행 기준으로 비교
    for i in range(n):
        count = 1
        for j in range(1, n):
            # 현재 사탕이 왼쪽 사탕하고 같으면
            if array[i][j] == array[i][j-1]:
                count += 1
                # max_count값 갱신
                if max_count < count:
                    max_count = count
            # 왼쪽하고 다르면 다시 count = 0
            else:
                count = 1
    # 1부터 마지막까지 열 기준으로 비교
    for j in range(0, n):
        count = 1
        for i in range(1, n):
            # 현재 사탕이 위쪽하고 같으면
            if array[i][j] == array[i-1][j]:
                count += 1
                # max_count값 갱신
                if max_count < count:
                    max_count = count
                # 왼쪽하고 다르면 다시 count = 0
            else:
                count = 1

    return max_count

# print(count_longest(arr))

ans = 0
# 행 기준으로 바꿈
for row in range(n):
    for col in range(1, n):
        # 매번 새로운 arr을 재할당
        new_arr = deepcopy(arr)
        new_arr[row][col], new_arr[row][col-1] = new_arr[row][col-1], new_arr[row][col]
        new_ans = count_longest(new_arr)
        if ans < new_ans:
            ans = new_ans

# 열 기준으로 바꿈
for row in range(1, n):
    for col in range(n):
        # 매번 새로운 arr을 재할당
        new_arr = deepcopy(arr)
        new_arr[row][col], new_arr[row-1][col] = new_arr[row-1][col], new_arr[row][col]
        new_ans = count_longest(new_arr)
        if ans < new_ans:
            ans = new_ans

print(ans)