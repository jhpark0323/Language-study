# k : 가지고 있는 랜선의 갯수, n : 필요한 랜선의 갯수
k, n = map(int, input().split())

ls = [int(input()) for _ in range(k)]

# print(ls)

# 최솟값
min_len = min(ls)

max_len_lansun = 0
lansun = 0
cnt = 0
# 가지고 있는 랜선 중 제일 작은 선의 길이만큼 순회
for i in range(1, min_len+1):
    cnt = 0

    # 모든 가지고 있는 랜선을 순회
    for j in ls:
        # print(j)
        # cnt에 랜선을 1부터 올라가며 계산해봄
        cnt += j // i
        if cnt == n:
            lansun = i
            # print(lansun)
            # 최댓값 갱신
            if max_len_lansun < lansun:
                max_len_lansun = lansun


        # cnt가 n보다 커지면 너무적음
        if cnt > n:
            break


print(max_len_lansun)