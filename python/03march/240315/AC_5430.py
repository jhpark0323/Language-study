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
        arr = list(arr.split(','))
    else:
        arr = []
    arr = deque(arr)
    # print('arr :', arr)

    try:
        dir = 0
        for i in func:
            if i == 'R':
                dir = 1 - dir
                # arr.reverse()
                # print(arr)

            else:
                if not dir:
                    arr.popleft()
                else:
                    arr.pop()

        if dir:
            arr.reverse()
            answer = '[' + ','.join(list(arr)) + ']'
            print(answer)
        else:
            answer = '[' + ','.join(list(arr)) + ']'
            print(answer)
    except:
        print('error')