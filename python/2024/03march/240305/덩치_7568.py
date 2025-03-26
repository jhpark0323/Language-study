n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
# print(arr)

rank = []
# 기준
for first in range(n):
    first_rank = n
    # 비교 대상
    for second in range(n):
        # 다른사람일 때만 비교
        if first != second:
            if arr[first][0] >= arr[second][0] or arr[first][1] >= arr[second][1]:
                first_rank -= 1
    rank.append(first_rank)

print(*rank)