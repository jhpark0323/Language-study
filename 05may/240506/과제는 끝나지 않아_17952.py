n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
# print(arr)

new_hw = 0
for hw in range(n):
    # 과제가 있다면
    if arr[hw][0]:
        # 새로운 과제 update
        new_hw = arr[hw][2]-1

    # 과제가 없을때
    else:
        # 앞에 하던 과제가 있으면
        pass

    new_hw -= 1

    # 과제를 끝내면
    if new_hw == 0:
