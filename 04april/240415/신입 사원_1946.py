T = int(input())

for _ in range(T):
    # 지원자의 숫자
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr.sort(reverse=True)
    # print(arr)

    arr.sort()

    cnt = 1
    max_ = arr[0][1]
    for i in range(1, n):
        if max_ > arr[i][1]:
            cnt += 1
            max_ = arr[i][1]

    print(cnt)

'''
1
5
1 5
2 3
3 4
4 2
5 1
'''