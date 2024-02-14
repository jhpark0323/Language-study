def binary_search(arr, n, key):
    start = 0  # 구간 초기화
    end = n-1

    # 검색 구간이 유효하면 반복
    while start <= end:
        # 중앙의 원소 인덱스
        middle = (start + end) // 2
        if arr[middle] == key:
            return middle  # middle의 index를 뽑음
        # 중앙값이 key보다 크면
        elif arr[middle] > key:
            end = middle - 1
        # 중앙값이 key보다 작으면
        else:
            start = middle + 1
    # 검색 실패
    return -1