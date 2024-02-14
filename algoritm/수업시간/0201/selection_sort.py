def selection_sort(a, n):
    # 구간의 시작을 i
    for i in range(n-1): # 2개의 원소가 남을 때 까지
        # 구간의 최솟값 위치 min_idx, 첫 원소를 최소로 가정
        min_idx = i
        # 실제 최솟값을 찾을 위치 j
        for j in range(i+1, n):  # i 다음 위치부터 j를 돌림
            if a[min_idx] > a[j]:
                min_idx = j
        a[min_idx], a[i] = a[i], a[min_idx]     # 최솟값을 구간의 맨 앞으로 이동


a = [3, 5, 7,3, 5, 24,14,23,4,1,3]
n = len(a)
print(a)    # [3, 5, 7, 3, 5, 24, 14, 23, 4, 1, 3]
selection_sort(a, n)
print(a)    # [1, 3, 3, 3, 4, 5, 5, 7, 14, 23, 24]