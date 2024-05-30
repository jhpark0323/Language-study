# index 조절이 아닌 list 자체를 조절한다.
def quick_sort(lst):
    # 정렬 대상을 분할해 나가다가
    # 더이상 분할 할 수 없는 상태가 되며, 해당 리스트 반환
    if len(lst) <= 1:
        return lst
    else:
        # 퀵 정렬의 pivot 위치는 아무 대상이어도 상관 없다.
        pivot = lst[0]
        # pivot보다 작은 대상만 모음
        less_than_pivot = [x for x in lst[1:] if x <= pivot]
        # pivot보다 큰 대상만 모음
        greater_than_pivot = [x for x in lst[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

arr = [3, 6, 8, 10, 1, 2, 1]
n = len(arr)
result = quick_sort(arr)
print(result)