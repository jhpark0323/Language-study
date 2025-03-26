from collections import deque

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
# print(arr)

arr.sort(key=lambda x: (x[1], x[0]))
arr = deque(arr)
# print(arr)

cnt = 1
while arr:
    end_time = arr.popleft()[1]
    # print('end_time: ', end_time)

    while arr:
        if arr[0][0] >= end_time:
            cnt += 1
            break
        start_time = arr.popleft()[0]

print(cnt)