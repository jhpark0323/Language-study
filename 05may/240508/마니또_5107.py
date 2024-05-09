test_case = 1
while True:
    n = int(input())
    if n == 0:
        break
    arr = [input().split() for _ in range(n)]
    # print(arr)

    new_ls = []
    cnt = 0
    for i in range(n):
        first, second = arr[i]
        # 첫번째가 new_ls에 있으면
        if first in new_ls:
            new_ls.append(second)

        # 두번째가 new_ls에 있으면
        if second in new_ls:
            new_ls.append(first)

        # 둘다 new_ls안에 없으면
        elif first not in new_ls and second not in new_ls:
            cnt += 1
            new_ls.append(first)
            new_ls.append(second)

    print(test_case, cnt)

    test_case += 1