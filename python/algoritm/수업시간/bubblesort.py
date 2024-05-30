n = 6
arr = [7, 2, 5, 3, 1, 4]


def asc(arr, n):
    # for i : n-1 -> 1, 정렬할 구간의 마지막 인덱스
    for i in range(n-1, 0, -1):
        # for j : 0 -> i-1, j 비교할 두 원소 중 왼쪽의 인덱스
        for j in range(i):
            # 오름차순은 큰 수를 오른쪽으로
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def dec(arr, n):
    # for i : n-1 -> 1, 정렬할 구간의 마지막 인덱스
    for i in range(n-1, 0, -1):
        # for j : 0 -> i-1, j 비교할 두 원소 중 왼쪽의 인덱스
        for j in range(i):
            # 내림차순은 작은 수를 오른쪽으로
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(asc(arr, n))
print(dec(arr, n))