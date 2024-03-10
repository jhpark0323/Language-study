def f(s):
    # 종료조건
    if s > k:
        return

    #
    elif s == k:
        return

    for i in range(n):
        for j in range(i, n):



n, k = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

ls = []