from collections import deque
import sys

input_data = sys.stdin.readline

T = int(input_data())

for test_case in range(T):
    func = input_data().strip()
    # print(func)
    n = int(input_data().strip())
    arr = input_data()
    arr = arr[1:-2]
    if arr:
        arr = list(map(int, arr.split(',')))
    else:
        arr = []
    arr = deque(arr)
    # print('arr :', arr)

    try:
        for i in func:
            if i == 'R':
                arr.reverse()
                # print(arr)

            else:
                arr.popleft()
                # print(arr)

        print(list(arr))
    except:
        print('error')