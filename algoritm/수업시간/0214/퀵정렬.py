def quick_sort(start, end):
    # 언제까지 조사할거냐
    # stack에 값이 있는 동안
    stack = [(start, end)]
    while stack:
        start, end = stack.pop()
        # 조사 번위가 꼬이지 않았다면
        if start < end:
            pivot_index = partition(start, end)
            # pivot 왼쪽 조사 대상
            stack.append((start, pivot_index - 1))
            stack.append((pivot_index + 1, end))

def partition(start, end):
    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] <= pivot:
            # 마지막에 pivot 위치의 값이 들어가야 할 위치
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[end] = arr[end], arr[i+1]

    return i+1

arr = [3, 6, 8, 10, 1, 2, 1]
n = len(arr)
quick_sort(0, n-1)
print(arr)