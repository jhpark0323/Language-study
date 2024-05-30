'''
이진 탐색
전체 arr를 기준으로 중앙값과 목표값(key)의 크기를 비교하여 start와 end를 계속 바꿔가며 찾아가는 탐색 방법
- arr이 (오름차순)정렬이 되어있어야함
'''

def binary_search_myself(arr, key):
    n = len(arr)
    # 시작점과 끝점 설정 -> index로
    start = 0
    end = n -1

    # 횟수를 세어줄 cnt 변수 할당
    cnt = 0

    # start와 end를 바꿔가며 계산 했을 때 start가 end를 넘어가면 반복 종료
    while start < end:
        # 중앙값 계산
        middle = (start + end) // 2

        # 중앙값이 key값과 같으면
        if arr[middle] == key:
            return (cnt, middle)

        # 중앙값이 key보다 크면
        elif arr[middle] > key:
            end = middle - 1

        # 중앙값이 key보다 작으면
        else:
            start = middle + 1

        cnt += 1
    return 'fail'