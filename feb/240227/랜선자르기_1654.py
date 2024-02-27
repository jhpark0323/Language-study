# k : 가지고 있는 랜선의 갯수, n : 필요한 랜선의 갯수
k, n = map(int, input().split())
ls = [int(input()) for _ in range(k)]
# print(ls)

# 가능한 랜선의 최대 길이 범위 설정
start, end = 1, max(ls)
max_len_lansun = 0

# 이진 탐색을 이용하여 최대 길이 찾기
while start <= end:
    mid = (start + end) // 2
    total = 0

    # mid 길이로 잘랐을 때 얻을 수 있는 랜선의 개수 계산
    for l in ls:
        total += l // mid

    # 필요한 랜선의 개수보다 많이 얻었으면 범위를 늘려서 길이를 늘림
    if total >= n:
        max_len_lansun = mid
        start = mid + 1
    # 필요한 랜선의 개수보다 부족하면 범위를 줄여서 길이를 줄임
    else:
        end = mid - 1

print(max_len_lansun)
